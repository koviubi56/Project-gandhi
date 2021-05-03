# -*- coding: utf-8 -*-
# coding: utf-8

"""
The main file.
Copyright (C) 2021  Koviubi56

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


def backup(type, get=False):
    if type == "CMD":
        db["backup"]["CMDbackup"] = {
            "szerdak": db["szerdak"],
            "time": time.asctime()
        }
    elif type == "AUTO":
        try:
            db["backup"]["AUTObackup"] = {
                "szerdak": db["szerdak"],
                "time": time.asctime()
            }
        except Exception as e:
            logging.error(str(e))
            return False
        else:
            logging.info("AutoBackup kész!")
            if get:
                return db["backup"]
            else:
                return True


while True:
    print("Starting...")
    try:
        import os
        import discord
        import random
        import dc
        import time
        from replit import db
        print("szerdak = \"{szerdak}\"; type(szerdak) = \"{szerdakT}\"; backup = \"{bu}\"; type(backup) = \"{buT}\"".format(
            szerdak=str(db["szerdak"]), szerdakT=str(type(db["szerdak"])), bu=str(db["backup"]), buT=str(type(db["backup"]))))

        print("=====")
        import logging
        logging.basicConfig(
            level=logging.INFO, format="[%(levelname)s %(name)s %(asctime)s line: %(lineno)d] %(message)s")
        logging = logging.getLogger(__name__)

        # ===SETTINGS===
        # Mennyi a maximális szerda amennyit elfogad egy üzenethez.
        maxSzerda = 510
        # Verzió
        version = "1.4.0"
        # Bármi más? PL: "-beta.1"?
        pre = "-beta.1"
        # Prefix
        prefix = "56!"
        # ---SETTINGS---

        client = discord.Client()

        for _ in range(80):
            print("\n")
        print("{:=^63}".format(f"GANDHI BOT {version}{pre}"))

        inGtn = False
        gtNum = 0
        inSet = False

        gandhi = [
            "Be the change that you wish to see in the world.",
            "Live as if you were to die tomorrow. Learn as if you were to live forever.",
            "An eye for an eye will only make the whole world blind.",
            "Happiness is when what you think, what you say, and what you do are in harmony.",
            "When I despair, I remember that all through history the way of truth and love have always won. There have been tyrants and murderers, and for a time, they can seem invincible, but in the end, they always fall. Think of it--always.",
            "The weak can never forgive. Forgiveness is the attribute of the strong.",
            "Where there is love there is life.",
            "Prayer is not asking. It is a longing of the soul. It is daily admission of one's weakness. It is better in prayer to have a heart without words than words without a heart.",
            "I like your Christ, I do not like your Christians. Your Christians are so unlike your Christ.",
            "Freedom is not worth having if it does not include the freedom to make mistakes.",
            "Nobody can hurt me without my permission.",
            "God has no religion.",
            "Hate the sin, love the sinner.",
            "I will not let anyone walk through my mind with their dirty feet.",
            """Your beliefs become your thoughts,
Your thoughts become your words,
Your words become your actions,
Your actions become your habits,
Your habits become your values,
Your values become your destiny.""",
            "You must not lose faith in humanity. Humanity is like an ocean; if a few drops of the ocean are dirty, the ocean does not become dirty.",
            "The best way to find yourself is to lose yourself in the service of others.",
            "The future depends on what you do today.",
            "A man is but the product of his thoughts. What he thinks, he becomes.",
            "To give pleasure to a single heart by a single act is better than a thousand heads bowing in prayer.",
            "The greatness of a nation and its moral progress can be judged by the way its animals are treated.",
            "Man often becomes what he believes himself to be. If I keep on saying to myself that I cannot do a certain thing, it is possible that I may end by really becoming incapable of doing it. On the contrary, if I have the belief that I can do it, I shall surely acquire the capacity to do it even if I may not have it at the beginning.",
            "Each night, when I go to sleep, I die. And the next morning, when I wake up, I am reborn.",
            "Earth provides enough to satisfy every man's needs, but not every man's greed.",
            "What difference does it make to the dead, the orphans and the homeless, whether the mad destruction is wrought under the name of totalitarianism or in the holy name of liberty or democracy?",
            "To believe in something, and not to live it, is dishonest.",
            "There are people in the world so hungry, that God cannot appear to them except in the form of bread.",
            "It is unwise to be too sure of one's own wisdom. It is healthy to be reminded that the strongest might weaken and the wisest might err.",
            "Whatever you do will be insignificant, but it is very important that you do it."
        ]

        @client.event
        async def on_ready():
            await client.change_presence(activity=discord.Game("Szőr"), status=discord.Status.online)
            print("-----")
            print("This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.")

            logging.info('Bejelentkezve: "{0.user}"'.format(client))

            backup("AUTO")

        @client.event
        async def on_message(message):
            if message.author == client.user:
                return

            plus = 0
            msg = message
            content = msg.content

            # hjelp
            if dc.cmd(msg, prefix, [
                ["hjelp", True],
                ["help", True],
                ["hjelp", False],
                ["@Gandhi", False],
                ["@Gandhi#0952", False],
                ["<@753651550047436902>", False],
                ["<@!753651550047436902>", False],
                ["<@&753651550047436902>", False]
            ]):
                if random.randrange(2) == 0:
                    await dc.send(msg, "Lottószámok (ötös lottó): || {} {} {} {} {} ||... vagy nem ezt kérdezed?".format(random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46)))
                elif random.randrange(2) == 0:
                    await dc.send(msg, "Lottószámok (hatos lottó): || {} {} {} {} {} {} ||... vagy nem ezt kérdezed?".format(random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46)))
                else:
                    await dc.send(msg, "Lottószámok (skandináv lottó): || {} {} {} {} {} {} {} ||... vagy nem ezt kérdezed?".format(random.randrange(1, 36), random.randrange(1, 36), random.randrange(1, 36), random.randrange(1, 36), random.randrange(1, 36), random.randrange(1, 36), random.randrange(1, 36)))
                embedHjelp = discord.Embed()
                embedHjelp.add_field(
                    name="8ball",
                    value=f"8ball/8labda\n__Szintaxis__: `{prefix}8ball `*<KÉRDÉS>*\n__PL__: `{prefix}8ball Szerda vanszk?`"
                )
                embedHjelp.add_field(
                    name="gtn",
                    value=f"Találd ki a számot\n__Szintaxis__: `{prefix}gtn `*<MAX SZÁM>*\n__PL__: `{prefix}gtn 756`"
                )
                embedHjelp.add_field(
                    name="kagi",
                    value=f":poop:\n__Szintaxis__: `{prefix}kagi`\n__PL__: `{prefix}kagi`"
                )

                await dc.embed(msg, embedHjelp)

            # szerda keresés
            try:
                for i, betu in enumerate(content):
                    if plus > maxSzerda:
                        logging.error("TÚL SOK SZERDA!")
                        await dc.send(
                            msg, f"Ez az üzenet annyira menő, hogy több mint {maxSzerda} szerda van benne.")
                        await dc.send(
                            msg, "|| Megjegyzés magamnak: *set*; szerdák: {szerdak} ||".format(szerdak=str(db["szerdak"])))
                        plus = 0
                        break
                    if (
                        betu.lower() == "s"
                        and content[i + 1] == "z"
                        and content[i + 2] == "e"
                        and content[i + 3] == "r"
                        and content[i + 4] == "d"
                        and content[i + 5] in ["a", "á"]
                    ):
                        plus += 1
                    continue
            except IndexError:
                pass

            if plus > 0:
                db["szerdak"] += plus
                await dc.send(msg, "+{plus} szerda (most: {szerdak})".format(plus=plus, szerdak=db["szerdak"]))

            # 56
            if content == "56":
                await dc.send(msg, f'Szerdák száma: {str(db["szerdak"])}')

            # stop
            if dc.cmd(msg, os.environ["KEY"], [
                ["stop", True]
            ]):
                await dc.send(msg, f'Szerdák: {str(db["szerdak"])}')
                logging.info("Creating backup...")
                try:
                    backup("AUTO")
                except Exception as e:
                    logging.error(f"Can't create backup! Error code: {e}")
                else:
                    logging.info("Stopping...")
                    exit()

            # set
            global inSet
            if inSet == True:
                inSet = False
                db["szerdak"] = int(content)
                logging.info("Szerda beállítva! Mostani szerda: \"{most}\"  Backup: \"{bu}\"".format(
                    most=db["szerdak"], bu=str(db["backup"])))

            if dc.cmd(msg, os.environ["KEY"], [
                ["set", True]
            ]):
                await dc.send(msg, "K!")
                inSet = True
                backup("AUTO")
                logging.warning(
                    "\"{}\" be akarja állítani a szerdák számát! Jelenleg \"{}\" szerda van! Jegyezd meg!".format(msg.author, db["szerdak"]))

            # makeBackup
            if dc.cmd(msg, os.environ["KEY"], [
                ["makebackup", True]
            ]):
                logging.warning(
                    "\"{}\" szeretne csinálni egy biztonsági mentést! Infókat lásd alább:".format(msg.author))
                print("MOST:szerdak = \"{szerda}\"; backup = \"{bu}\"".format(
                    szerda=db["szerdak"], bu=db["backup"]))
                BUlesz = db["backup"]
                BUlesz["CMDbackup"] = {
                    "szerdak": db["szerdak"],
                    "time": time.asctime()
                }
                print("LESZ: backup = \"{}\"".format(str(BUlesz)))
                backup("CMD")
                logging.info("Backup kész!")
                await dc.send(msg, "Backup kész!")

            # resetBackup
            if dc.cmd(msg, os.environ["KEY"], [
                ["resetbackup", True]
            ]):
                logging.warning(
                    "\"{}\" resetelni akarja a backupot! Infókat lásd alább!".format(str(msg.author)))
                print("MOST: backup = \"{}\"".format(str(db["backup"])))
                print("LESZ: backup = \"{}\"".format(str(
                    {"CMDbackup": {}, "AUTObackup": {}}
                )))
                db["backup"] = {
                    "CMDbackup": {},
                    "AUTObackup": {}
                }
                await dc.send(msg, "Kész!")

            global inGtn
            if inGtn:
                global gtNum
                if int(content) == int(gtNum):
                    inGtn = False
                    await dc.send(msg, "Jippí!")
                    await dc.send(msg, "Lottószámok (ötös lottó): || {} {} {} {} {} ||".format(random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46)))
                elif int(content) > int(gtNum):
                    await dc.send(msg, "Kisebb!")
                elif int(content) < int(gtNum):
                    await dc.send(msg, "Nagyobb!")

            # getBackup
            if dc.cmd(msg, prefix, [
                ["getbackup", True]
            ]):
                logging.warning(
                    "Valaki meg akarja nézni a biztonsági mentést!")
                await dc.send(msg, "Backup:\n```json\n{}\n```".format(str(db["backup"])))

            # 8ball
            if dc.cmd(msg, prefix, [
                ["8ball", True]
            ]):
                if len(msg.content) > len(prefix) + len("8ball "):
                    lista8 = [
                        "ez pokolian nem",
                        "őszintén szólva nem érdekel lol",
                        "nem vagyok benne biztos, de te biztos, hogy hülye vagy",
                        "igen???",
                        "amikor növesztessz egy agysejtet, akkor igen",
                        "nem!!!!",
                        "lol szó szerint nem",
                        "a fenébe! nem.",
                        "persze miért ne",
                        "nem lmfao",
                        "persze, engem se érdekel jobban",
                        "Trump színe narancssárga?",
                        "én egy 8ball labda vagyok, nem foglalkozok a szar labdáiddal",
                        "biztos forrásból tudom: nem",
                        "biztos forrásból tudom: igen",
                        "egy szőrszálamnak több IQ-ja van te barom",
                        "még egy hüje kérdés bedoblak tehén tápnak",
                        # ˇ1.3.0-beta.4
                        "kérdezd meg később amikor nem leszek elfoglalva anyáddal",
                        "igen!!!!",
                        "igen, idióta",
                        "nem, idióta",
                        "a fené(k)be!!",
                        "nem???",
                        # ˇ1.4.0-beta,1
                        "π + 7^5 / 6",
                        "-. . ...- . .-. / --. --- -. .- / --. .. ...- . / -.-- --- ..- / ..- .--. -.-.--",
                        "4E 45 56 45 72 / 47 4F 4E 4E 41 / 4C 45 54 / 59 4F 55 / 44 4F 57 4E"
                    ]
                    embed8ball = discord.Embed()
                    #       0123456789
                    # PREFIX8ball xyz
                    embed8ball.add_field(name=msg.content[len(
                        prefix) + 6:], value=random.choice(lista8))
                    await dc.embed(msg, embed8ball)
                else:
                    await dc.send(msg, "Írjál má' kérdést te hónaljszagú ogre!")
                    await dc.send(msg, f"Így használd: `{prefix}8ball `*<KÉRDÉS>*")
                    await dc.send(msg, f"PL: `{prefix}8ball Szerda van?`")

            # gtn
            if dc.cmd(msg, prefix, [
                ["gtn", True]
            ]):
                if len(msg.content) <= len(prefix) + len("gtn") + 1:
                    await dc.send(msg, "Mennyi legyen a max szám? He?!")
                    await dc.send(msg, f"Így használd: `{prefix}gtn `*<MAX SZÁM>*")
                    await dc.send(msg, f"PL: `{prefix}gtn 756`")
                else:
                    gtNum = random.randrange(
                        1, int(msg.content[len(prefix) + 4:]))
                    inGtn = True
                    await dc.send(msg, "A nyeremény a lottó számok. Hajrá!")

            # kagi
            if dc.cmd(msg, prefix, [
                ["kagi", True]
            ]):
                await dc.send(msg, ":poop:")

            # bölcsesség
            if dc.cmd(msg, prefix, [
                ["bölcsesség", True],
                ["bolcsesseg", True],
                ["idézet", True],
                ["idezet", True],
                ["quote", True]
            ]):
                quoteE = discord.Embed()
                quoteE.add_field(name="Bölcsesség Gandhi-tól",
                                 value=random.choice(gandhi))
                await dc.embed(msg, quoteE)

        client.run(os.environ["BOT_TOKEN"])

    except Exception as e:
        print("\n\n[ERROR]")
        print(f"Error code: \"{str(e)}\"")
        print("Újraindítás...")
        continue
