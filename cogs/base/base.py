import datetime

import discord
from discord.ext import commands, tasks

from cogs.resource import CogConfig, CogText
from core import rubbercog, utils
from core.config import config

boottime = datetime.datetime.now().replace(microsecond=0)


class Base(rubbercog.Rubbercog):
    """About"""

    def __init__(self, bot: commands.Bot):
        super().__init__(bot)

        self.config = CogConfig("base")
        self.text = CogText("base")

        self.status_loop.start()
        self.status = "online"

    def cog_unload(self):
        self.status_loop.cancel()

    ##
    ## Loops
    ##

    @tasks.loop(minutes=1)
    async def status_loop(self):
        """Observe latency to the Discord API. If it goes below 0.4s, "online"
        will be switched to "idle", over 0.8s is "busy".
        """
        if self.bot.latency <= 0.4:
            status = "online"
        elif self.bot.latency <= 0.8:
            status = "idle"
        else:
            status = "busy"

        if self.status != status:
            await utils.set_presence(self.bot, getattr(discord.Status, status))

    @status_loop.before_loop
    async def before_status_loop(self):
        if not self.bot.is_ready():
            await self.bot.wait_until_ready()

    ##
    ## Commands
    ##

    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    @commands.command()
    async def uptime(self, ctx):
        """Bot uptime"""
        now = datetime.datetime.now().replace(microsecond=0)
        delta = now - boottime

        embed = self.embed(ctx=ctx)
        embed.add_field(name="Boot", value=str(boottime), inline=False)
        embed.add_field(name="Uptime", value=str(delta), inline=False)
        await ctx.send(embed=embed)
        await utils.delete(ctx.message)

    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    @commands.command()
    async def ping(self, ctx):
        """Bot latency"""
        await ctx.reply("pong: **{:.2f} s**".format(self.bot.latency))

    ##
    ## Listeners
    ##

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        """Pinning functionality"""
        channel = self.bot.get_channel(payload.channel_id)
        if channel is None or not isinstance(channel, discord.TextChannel):
            return
        try:
            message = await channel.fetch_message(payload.message_id)
        except discord.NotFound:
            return
        if payload.emoji.is_custom_emoji():
            return
        reaction_author: discord.User = self.bot.get_user(payload.user_id)

        if payload.emoji.name == "📍" and not reaction_author.bot:
            await reaction_author.send(self.text.get("bad pin"))
            return await message.remove_reaction(payload.emoji, reaction_author)

        if payload.emoji.name != "📌":
            return

        for reaction in message.reactions:
            if reaction.emoji == "📍" and self.bot.user in await reaction.users().flatten():
                return await message.remove_reaction(payload.emoji, reaction_author)

            if reaction.emoji != "📌":
                continue

            if message.pinned:
                return await reaction.clear()

            if channel.id in self.config.get("unpinnable"):
                return await reaction.clear()

            if reaction.count < self.config.get("pins"):
                return

            users = await reaction.users().flatten()
            user_names = ", ".join([str(user) for user in users])
            log_embed = self.embed(title=self.text.get("pinned"), description=user_names)
            if len(message.content):
                value = utils.id_to_datetime(message.id).strftime("%Y-%m-%d %H:%M:%S")
                log_embed.add_field(name=str(message.author), value=value)
            url_text = self.text.get(
                "link text",
                channel=channel.name,
                guild=channel.guild.name,
            )
            if len(message.content):
                log_embed.add_field(
                    name=self.text.get("content"),
                    value=message.content[:1024],
                    inline=False,
                )
            if len(message.content) >= 1024:
                log_embed.add_field(
                    name="\u200b",
                    value=message.content[1024:],
                    inline=False,
                )
            if len(message.attachments):
                log_embed.add_field(
                    name=self.text.get("content"),
                    value=self.text.get("attachments", count=len(message.attachments)),
                    inline=False,
                )
            log_embed.add_field(
                name=self.text.get("link"),
                value=f"[{url_text}]({message.jump_url})",
                inline=False,
            )

            try:
                await message.pin()
            except discord.errors.HTTPException as e:
                await self.event.user(channel, "Could not pin message.", e)
                error_embed = self.embed(
                    title=self.text.get("pin error"),
                    description=user_names,
                    url=message.jump_url,
                )
                await message.channel.send(embed=error_embed)
                return

            event_channel = self.bot.get_channel(config.get("channels", "events"))
            await event_channel.send(embed=log_embed)

            await reaction.clear()
            await message.add_reaction("📍")
