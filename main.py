# -*- coding: utf-8 -*-
# coding: utf-8

"""
This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
"""


def backup(type):
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
        else:
            logging.info("AutoBackup kész!")


while True:
    print("Starting...")
    try:
        import os
        import discord
        import random
        import dc
        import time
        from replit import db

        print("=====")
        import logging
        logging.basicConfig(
            level=logging.INFO, format="[%(levelname)s %(name)s %(asctime)s line: %(lineno)d] %(message)s")
        logging = logging.getLogger(__name__)

        logging.info("szerdak = {szerdak}; type(szerdak) = {szerdakT}; backup = {bu}; type(backup) = {buT}".format(
            szerdak=str(db["szerdak"]), szerdakT=str(type(db["szerdak"])), bu=str(db["backup"]), buT=str(type(db["backup"]))))

        try:
            x = type(db["szerdak"])
            if x is None:
                print("Type of x: ".format(str(type(x))))
                backup()
                db["szerdak"] = 0
        except Exception as e:
            print(f"NOT_PROBLEM0 error: {e}")
            db["szerdak"] = 0
        finally:
            inSet = False

        # ===SETTINGS===
        # Mennyi a maximális szerda amennyit elfogad egy üzenethez.
        maxSzerda = 510
        # Verzió
        version = "1.3.0"
        # Bármi más? "-beta.1"?
        pre = "-beta.3"
        # Prefix
        prefix = "56!"
        # ---SETTINGS---

        client = discord.Client()

        for _ in range(80):
            print("\n")
        print("{:=^63}".format(f"GANDHI BOT {version}{pre}"))

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
            """Let the first act of every morning be to make the following resolve for the day:

- I shall not fear anyone on Earth.
- I shall fear only God.
- I shall not bear ill will toward anyone.
- I shall not submit to injustice from anyone.
- I shall conquer untruth by truth. And in resisting untruth, I shall put up with all suffering.""",
            "The future depends on what you do today.”",
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
            print("-----")
            print('This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.')

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
            if dc.cmd(msg, prefix, "hjelp") or content == "@Gandhi" or content == "<@!753651550047436902>":
                if content == "@Gandhi":
                    await dc.send(msg, "Úgy látom valaki megidézett!")

                if random.randrange(3) == 0:
                    await dc.send(msg, "Lottószámok (ötös lottó): || {} {} {} {} {} ||... vagy nem ezt kérdezed?".format(random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46)))
                elif random.randrange(3) == 1:
                    await dc.send(msg, "Lottószámok (hatos lottó): || {} {} {} {} {} {} ||... vagy nem ezt kérdezed?".format(random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46)))
                elif random.randrange(3) == 1:
                    await dc.send(msg, "Lottószámok (skandináv lottó): || {} {} {} {} {} {} {} ||... vagy nem ezt kérdezed?".format(random.randrange(1, 36), random.randrange(1, 36), random.randrange(1, 36), random.randrange(1, 36), random.randrange(1, 36), random.randrange(1, 36), random.randrange(1, 36)))

                await dc.send(msg, f""" **Prefix**: {prefix}
**Verzió**: {version}{pre}
**__Parancsok__**: 
**56**: Kiírja az eddig számolt szerdákat
**{prefix}8ball**: 8ball/8labda
                              """)

                await dc.send(msg, """És ne feledd:
> "{}"
    ― Mahatma Gandhi
""".format(random.choice(gandhi)))

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
                    if betu.lower() == "s":
                        if content[i + 1] == "z":
                            if content[i + 2] == "e":
                                if content[i + 3] == "r":
                                    if content[i + 4] == "d":
                                        if content[i + 5] == "a" or content[i + 5] == "á":
                                            plus += 1
                                            continue
                                        else:
                                            continue
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                continue
                        else:
                            continue
                    else:
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
            if dc.cmd(msg, os.environ["KEY"], "stop"):
                await dc.send(msg, f'Szerdák: {str(db["szerdak"])}')
                logging.info("Stopping...")
                exit()

            # set
            global inSet
            if inSet == True:
                inSet = False
                db["szerdak"] = int(content)
                logging.info("Szerda beállítva! Mostani szerda: {most}  Backup: {bu}".format(
                    most=db["szerdak"], bu=str(db["backup"])))

            if dc.cmd(msg, os.environ["KEY"], "set"):
                await dc.send(msg, "K!")
                inSet = True
                backup()
                logging.warning(
                    "{} be akarja állítani a szerdák számát! Jelenleg {} szerda van! Jegyezd meg!".format(msg.author, db["szerdak"]))

            # makeBackup
            if dc.cmd(msg, os.environ["KEY"], "makebackup"):
                logging.warning(
                    "{} szeretne csinálni egy biztonsági mentést! Infókat lásd alább:".format(msg.author))
                print("MOST:szerdak = {szerda}; backup = {bu}".format(
                    szerda=db["szerdak"], bu=db["backup"]))
                BUlesz = db["backup"]
                BUlesz["CMDbackup"] = {
                    "szerdak": db["szerdak"],
                    "time": time.asctime()
                }
                print("LESZ: backup = {}".format(str(BUlesz)))
                db["backup"] = {}

            # resetBackup
            if dc.cmd(msg, os.environ["KEY"], "resetbackup"):
                logging.warning(
                    "{} resetelni akarja a backupot! Infókat lásd alább!".format(str(msg.author)))
                print("MOST: backup = \"{}\"".format(str(db["backup"])))
                print("LESZ: backup = \"{}\"".format(str(
                    {"CMDbackup": {}, "AUTObackup": {}}
                )))
                db["backup"] = {
                    "CMDbackup": {},
                    "AUTObackup": {}
                }
                await dc.send(msg, "Kész!")

            # getBackup
            if dc.cmd(msg, prefix, "getbackup"):
                logging.warning(
                    "{} meg akarja nézni a biztonsági mentést!".format(msg.author))
                await dc.send(msg, """Backup: 
```json
{}
```""".format(str(db["backup"])))

            # 8ball
            if dc.cmd(msg, prefix, "8ball"):
                if len(content) > len(prefix) + len("8ball "):
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
                        "biztos forrásból tudom: igen"
                    ]
                    embed8ball = discord.Embed()
                    #       0123456789
                    # PREFIX8ball xyz
                    embed8ball.add_field(
                        name=content[len(prefix) + 6:], value=random.choice(lista8))
                    await dc.embed(msg, embed8ball)
                else:
                    await dc.send(msg, ":(")
                    await dc.send(msg, f"Így használd: `{prefix}8ball `*<KÉRDÉS>*")
                    await dc.send(msg, f"PL: `{prefix}8ball Szerda van?`")

        client.run(os.environ["BOT_TOKEN"])

    except Exception as e:
        print("\n\n")
        logging.error(f"Error code: {str(e)}")
        logging.info("Újraindítás...")
        continue
