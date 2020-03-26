from config import config


class Messages:
    prefix = config.Config.default_prefix

    server_warning = "Tohle funguje jen na VUT FIT serveru."
    karma_get_missing = "Toaster pls, měls bordel v DB. Musel jsem za tebe uklidit."
    missing_perms = "Na tohle nemas prava. {user}"
    acl_help = "{user}, Pouziti:\n`!acl {{action}} {{table}} [args]`\n"\
               "action: add, edit, del nebo list\n"\
               "table: group, rule, role nebo user\n"\
               "args zalezi na zvolene akci a tabulce, napriklad kdyz chcete"\
               "pridat groupu, musite zadat nazev groupy a nepovinne take "\
               "ID rodice jako argumnet"  # TODO: Correct to proper czech
    acl_add_group = "Group vytvorena."
    acl_edit_group = "Group zmenena."
    acl_del_group = "Group smazana."
    acl_add_rule = "Pravidlo vytvoreno."
    acl_edit_rule = "Pravidlo zmeneno."
    acl_del_rule = "Pravidlo smazano."
    acl_add_role = "Vyjimka pro roli pridana."
    acl_edit_role = "Vyjimka pro roli upravena."
    acl_del_role = "Vyjimka pro roli smazana."
    acl_add_user = "Vyjimka pro uzivatele pridana."
    acl_edit_user = "Vyjimka pro uzivatele upravena."
    acl_del_user = "Vyjimka pro uzivatele smazana."
    no_such_command = "Takový příkaz neznám. <:sadcat:691413849978568724>"
    spamming = "{user} Nespamuj tolik <:sadcat:691413849978568724>"
    insufficient_rights = "{user}, na použití tohoto příkazu nemáš právo."
    vote_room_only = "Tohle funguje jen v {room}."
    bot_room_redirect = "{user} <:sadcat:691413849978568724> 👉 " \
                        "<#{bot_room}>\n"
    message_link_prefix = 'https://discordapp.com/channels/' \
                          + str(config.Config.guild_id) + '/'

    uhoh_counter = "{uhohs} uh ohs od spuštění."
    uptime_message = "Up since:  `{boottime}`\nUptime:\t`{uptime}`"

    kachna_grillbot = "<:wutcat:692496001155596388> Běž na FIT."

    karma = "{user} Karma uzivatele `{target}` je: **{karma}** " \
            "(**{order}.**)\nA rozdal:\n" \
            "**{karma_pos}** pozitivní karmy " \
            "(**{karma_pos_order}.**)\n" \
            "**{karma_neg}** negativní karmy " \
            "(**{karma_neg_order}.**)"

    karma_invalid_command = "Neznámý karma příkaz."
    karma_vote_format = "Neočekávám argument. " \
                        "Správný formát: `" + prefix + "karma vote`"
    karma_vote_message_hack = "Hlasování o karma ohodnocení emotu"
    karma_vote_message = karma_vote_message_hack + " {emote}"
    karma_vote_info = "Hlasování skončí za **{delay}** " \
                      "minut a minimální počet hlasů je " \
                      "**{minimum}**."
    karma_vote_result = "Výsledek hlasování o emotu {emote} " \
                        "je {result}."
    karma_vote_notpassed = "Hlasovani o emotu {emote} neprošlo\n" \
                           "Aspoň {minimum} hlasů potřeba."
    karma_vote_allvoted = "Už se hlasovalo o všech emotech."
    karma_revote_format = "Očekávám pouze formát: " \
                          "`" + prefix + "karma revote [emote]`"
    karma_emote_not_found = "Emote jsem na serveru nenašel."
    karma_get_format = "Použití:\n" \
                       "`" + prefix + "karma get`: " \
                       "vypíše všechny emoty s hodnotou.\n" \
                       "`" + prefix + "karma get [emote]`: " \
                       "vrátí hodnotu daného emotu."
    karma_get = "Hodnota {emote} je {value}."
    karma_get_emote_not_voted = "{emote} není ohodnocen."
    karma_give_format = "Toaster pls, formát je " \
                        "`" + prefix + "karma give [number] [user(s)]`"
    karma_give_format_number = "Toaster pls, formát je " \
                               "`" + prefix + "karma give " \
                               "[number, jakože číslo, " \
                               "ne {input}] [user(s)]` "
    karma_give_success = "Karma byla úspěšně přidaná."
    karma_give_negative_success = "Karma byla úspěšně odebraná."
    karma_message_format = prefix + "karma message [url, id]"
    member_not_found = "{user} Nikoho takového jsem nenašel."
    karma_lederboard_offser_error = "{user} Špatný offset, zadej kladné číslo"

    role_add_denied = "{user}, na přidání role {role} nemáš právo."
    role_remove_denied = "{user}, " \
                         "na odebrání role {role} nemáš právo."
    role_invalid_line = "{user}, řádek `{line}` je neplatný."
    role_format = "{user}, použij `!god`."
    role_not_on_server = "Nepíšeš na serveru, " \
                         "takže předpokládám, " \
                         "že myslíš role VUT FIT serveru."
    role_not_role = "{user}, {not_role} není role."
    role_invalid_emote = "{user}, {not_emote} " \
                         "pro roli {role} není emote."

    rng_generator_format = "Použití: `" + prefix + "roll x [y]`\n" \
                           "x, y je rozmezí čísel,\n" \
                           "x, y jsou celá čísla,\n" \
                           "pokud y není specifikováno, " \
                           "je považováno za 0."
    rng_generator_format_number = "{user}, zadej dvě celá čísla, " \
                                  "**integers**."

    rd_too_many_dice_in_group = "Příliš moc kostek v jedné " \
                                "skupině, maximum je {maximum}."
    rd_too_many_dice_sides = "Příliš moc stěn na kostkách, " \
                             "maximum je {maximum}."
    rd_too_many_dice_groups = "Příliš moc skupin kostek, " \
                              "maximum je {maximum}."
    rd_format = "Chybná syntax hodu ve skupině {group}."
    rd_help = "Formát naleznete na " \
              "https://wiki.roll20.net/Dice_Reference\n" \
              "Implementovány featury podle obsahu: **8. Drop/Keep**"

    verify_already_verified = "{user} Už jsi byl verifikován ({admin} pls)."
    verify_send_format = "Ocekavam jeden argument. Správný formát:\n" \
                           "`{}verify [xlogin00|UČO]`".format(prefix)
    verify_send_dumbshit = "{user} Tvůj login. {emote}"
    verify_send_success = "{user} Kód byl odeslán na tvůj mail " + \
                          "({mail})!\n" + \
                          "Pro verifikaci použij: " + \
                          "`" + prefix + "verify [login] [kód]`"
    verify_send_not_found = "{user} Login nenalezen nebo jste tímto krokem již prošli ({admin} pls)."
    verify_verify_format = "Očekávám tři argumenty. " + \
                           "Správný formát:\n" + \
                           "`{}verify [xlogin00|UČO]`\n\n".format(prefix) + \
                           "Pro získání kódu použij příkaz podle příslušnosti:\n" + \
                           "`{}getcode [FEKT] [xlogin00]`\n".format(prefix) + \
                           "`{}getcode [VUT]  [xlogin00]`\n".format(prefix) + \
                           "`{}getcode [MUNI] [UČO]`\n".format(prefix) + \
                           "`{}getcode jine host`".format(prefix)
    verify_verify_dumbshit = "{user} Kód, který ti přišel na mail. {emote}"
    verify_verify_manual = "Čauec {user}, nechám {admin}, " \
                           "aby to udělal manuálně, " \
                           "jsi shady (Year: {year})"
    verify_verify_success = "{user} Gratuluji k verifikaci!"
    verify_post_verify_fekt = "Obor si zapiš v <#692086702382121010>\n" \
                              "V <#692084608778633217> získáš další role pro zájmy\n" \
                              "Obecné informace jsou v <#692084651849678938>."
    verify_post_verify_guest = "V <#692084608778633217> získáš další role pro zájmy\n" \
                              "Obecné informace jsou v <#692084651849678938>."

    verify_verify_not_found = "{user} Login nenalezen nebo " \
                              "jsi už tímhle krokem prošel " \
                              "({admin} pls)."
    verify_verify_wrong_code = "{user} Špatný kód."

    vote_format = "Použití vote:\n`" + prefix + "vote [datum] [čas] [otázka]\n[emoji]" \
                                                " [odpověď 1]\n[emoji] [odpověď 2]\na tak dále`\n" \
                                                "Datum je ve formátu `dd.MM.(yy)`. Čas je ve formátu `hh:mm`. " \
                                                "Pouze vyplněný čas použije den odeslání zprávy, " \
                                                "pouze vyplněné datum použije čas 00:00. " \
                                                "Datum a čas jsou nepovinné argumenty, " \
                                                "hlasování bude bez jejich uvedení funkční neustále. " \
                                                "Pokud jsou vyplněny, bot pošle po uplynutí zprávu o výsledku," \
                                                "když ho mezitím nikdo nevypne. " \
                                                "Indikace výherné možnosti přežije i vypnutí."
    vote_not_emoji = "{not_emoji} není emoji. <:sadcat:691413849978568724>"
    vote_bad_date = "Hlasování může skončit jen v budoucnosti. <:objection:692102817120518145>"

    vote_winning = "Prozatím vyhrává možnost {winning_emoji} „{winning_option}“ s {votes} hlasy."
    vote_winning_multiple = "Prozatím vyhrávají možnosti {winning_emojis} s {votes} hlasy."

    vote_none = "Čekám na hlasy."

    vote_result = "V hlasování „{question}“ vyhrála možnost {winning_emoji} „{winning_option}“ s {votes} hlasy."
    vote_result_multiple = "V hlasování „{question}“ vyhrály možnosti {winning_emojis} s {votes} hlasy."
    vote_result_none = "V hlasování „{question}“ nikdo nehlasoval. <:sadcat:691413849978568724>"

    review_format = prefix + "reviews [add, remove, zkratka předmětu]"
    review_add_format = prefix + "reviews add {ZkratkaPredmetu} {Tier (0-4, 0 je TOP)} (anonym - Pokud si přejete anonymní příspěvek) (VolitelnyText)\n" \
                        "Například:\nPro anonymní příspěvek: `" + prefix +"reviews add ITU 0 anonym text recenze`\n" \
                        "Jinak: `" + prefix +"reviews add IZP 2 text recenze`"

    review_wrong_subject = "Nesprávná zkratka předmětu"
    review_tier = "Tier je z rozsahu 0-4, kde 0 je nejlepší"
    review_text_len = "Maximální počet znaků v části 'text' je 1024"
    review_added = "Hodnocení předmětu bylo přidáno"
    reviews_page_e = "Zavolej znova reviews pro aktualizaci"

    review_get_format = prefix + "reviews [zkratka předmětu]"
    review_remove_format = prefix + "reviews remove [zkratka předmětu]"
    review_remove_format_admin = prefix + "reviews remove [zkratka předmětu, id + číslo]"
    review_remove_id_format = "reviews remove id [id]"
    review_remove_success = "Hodnocení předmětu bylo odebráno"
    review_remove_error = "Hodnocení předmětu nebylo nalezeno"
    review_add_denied = "{user}, na přidání hodnocení předmětu nemáš právo."
    subject_format = prefix + "subject [add, remove] [zkratka předmětu]"

    pr_meme = "https://github.com/sinus-x/rubbergoddess/pulls"
    uhoh = "uh oh"
    question = ["nech mě <:sadcat:691413849978568724>"]
    
    name_day_cz = "Dnes má svátek {name}"
    name_day_sk = "Dnes má meniny {name}"

    info = [[('karma', 'Vypíše vaši karmu, kolik pozitivní a negativní karmy'
                       ' jste rozdali.'),
             ('karma stalk [user]', 'Vypíše karmu uživatele, kolik pozitivní '
                                    'a negativní karmy rozdal.'),
             ('karma get',
              'Vypíše, které emoty mají hodnotu 1 a -1.'),
             ('karma get [emote]',
              'Vrátí karma hodnotu emotu.'),
             ('karma vote',
              'Odstartuje hlasování o hodnotě zatím neohodnoceného emotu.'),
             ('karma revote [emote]',
              'Odstartuje hlasování o nové hodnotě emotu.'),
             ('karma message [url, id]',
              'Zobrazí karmu získanou za zprávu')],
            [('leaderboard [offset]', 'Karma leaderboard'),
             ('bajkarboard [offset]', 'Karma leaderboard reversed'),
             ('givingboard [offset]', 'Leaderboard rozdávání pozitivní karmy.'),
             ('ishaboard [offset]', 'Leaderboard rozdávání negativní karmy.'),
             (review_add_format[1:], 'Přidá recenzi na předmět.'),
             (review_get_format[1:], 'Vypíše recenze na vybraný předmět.'),
             (review_remove_format[1:], 'Odstraní hodnocení.'),
             ('vote', 'Zahájí hlasování.')],
            [('roll X Y',
              'Vygeneruje náhodné celé číslo z intervalu <**X**, **Y**>.'),
             ('flip', 'Hodí mincí'),
             ('pick *Is foo bar? Yes No Maybe*',
              'Vybere jedno ze slov za otazníkem.'),
             ('diceroll', 'Všechno možné házení kostkami.'),
             ('week', 'Vypíše, kolikátý je zrovna týden '
                      'a jestli je sudý nebo lichý.'),
             ('uhoh', 'Vypíše počet uh ohs od spuštění.'),
             ('uptime', 'Vypíše čas spuštění a čas uplynulý od spuštění.'),
             ('kachna', 'Vypíše čas do otevření kachny.'),
             ('god', 'Vypíše tuto zprávu.')]]
