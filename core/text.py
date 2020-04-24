import json, re

import discord

from config.emote import emote
from config.config import config

class Text:
    """Manage string values"""
    def __init__(self):
        self.default = json.load(open('config/text.default.json', 'r'))
        try:
            self.custom = json.load(open('config/text.json', 'r'))
        except FileNotFoundError:
            self.custom = None

    def get(self, group: str, key: str):
        # load string
        if self.custom is not None and \
           group in self.custom and key in self.custom.get(group):
            string = self.custom.get(group).get(key)
        elif group in self.default and key in self.default.get(group):
            string = self.default.get(group).get(key)
        else:
            return None

        return self._replace(string)

    def fill(self, group: str, key: str, **kwargs):
        string = self.get(group, key)

        if 'user' in kwargs:
            kwargs['user'] = self._mention_user(kwargs['user'])
        if 'admin' in kwargs:
            kwargs['admin'] = self._mention_user(config.admin_id)
        if 'role' in kwargs:
            kwargs['role'] = self._mention_role(kwargs['role'])
        if 'channel' in kwargs:
            kwargs['channel'] = self._mention_channel(kwargs['channel'])

        for key in kwargs:
            if "{"+key+"}" in string:
                string = string.replace("{"+key+"}", kwargs[key])
        return string


    def _replace(self, string: str):
        # substitute emotes
        emotes = re.findall(r"{emote\.([a-z]+)}", string)
        for e in emotes:
            string = string.replace("{emote."+e+"}", emote.get(e))

        # substitute prefix
        string = string.replace("{prefix}", config.prefix)

        return string

    def _mention_user(self, user):
        if isinstance(user, discord.Member):
            return user.mention
        if isinstance(user, int):
            return f"<@{user}>"
        return str(user)

    def _mention_channel(self, channel):
        if isinstance(channel, discord.TextChannel) \
        or isinstance(channel, discord.VoiceChannel):
            return channel.mention
        if isinstance(channel, int):
            return f"<#{discord_id}>"
        return str(channel)

    def _mention_role(self, role):
        if isinstance(role, discord.Role):
            return role.mention
        if isinstance(role, int):
            return f"<@&{discord_id}>"
        return str(role)


text = Text()