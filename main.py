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
        try:
            from replit import db
        except Exception as e:
            import logging
            logging.error(
                f"Nem sikerült a db-t importálni a replit-ből: {str(e)}")
            logging.info("Újrapróbálkozás...")
            for e2 in range(5):
                try:
                    from replit import db
                except:
                    if e2 < 4:
                        logging.error(f"[ERROR {e2} ]")
                    elif e2 >= 4:
                        logging.critical(
                            "Nem sikerült importálni 6 alkalommal se. A bot e nélkül NEM működik.")
                        logging.info("Leállítás...")
                        exit()
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
        print('{:=^63}'.format(f'GANDHI BOT {version}{pre}'))

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
            if content == '56':
                await dc.send(msg, f'Szerdák száma: {str(db["szerdak"])}')

            # stop
            if dc.cmd(msg, os.environ['KEY'], 'stop'):
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

            if dc.cmd(msg, os.environ['KEY'], 'set'):
                await dc.send(msg, 'K!')
                inSet = True
                backup()
                logging.warning(
                    "{} be akarja állítani a szerdák számát! Jelenleg {} szerda van! Jegyezd meg!".format(msg.author, db["szerdak"]))

            # makeBackup
            if dc.cmd(msg, os.environ['KEY'], "makebackup"):
                logging.warning(
                    "{} szeretne csinálni egy biztonsági mentést! Infókat lásd alább:".format(msg.author))
                print("MOST:szerdak = {szerda}; backup = {bu}".format(
                    szerda=db["szerdak"], bu=db["backup"]))
                print("LESZ: backup = {}".format(str(
                    {
                        "szerdak": db["szerdak"],
                        "time": time.asctime()
                    }
                )))
                db["backup"] = {}

            # resetBackup
            if dc.cmd(msg, os.environ['KEY'], "resetbackup"):
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
                dc.send(msg, "Kész!")

            # getBackup
            if dc.cmd(msg, prefix, "getbackup"):
                logging.warning(
                    "{} meg akarja nézni a biztonsági mentést!".format(msg.author))
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ! README: A {} .:!DIREKT!:. van ott, és úgy !
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                await dc.send(msg, """Backup: 
                              ```json
{}
                              ```""".format(str(db["backup"])))
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ! README: A {} .:!DIREKT!:. van ott, és úgy !
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            # 8ball
            if dc.cmd(msg, prefix, "8ball"):
                lista8 = [
                    "ez%20pokolian%20nem",
                    "őszintén%20szólva%20nem%20érdekel%20lol",
                    "nem%20vagyok%20benne%20biztos,%20de te biztos,%20hogy%20hülye%20vagy",
                    "igen???",
                    "amikor%20növesztessz%20egy%20agysejtet,%20akkor%20igen",
                    "nem!!!!",
                    "lol%20szó%20szerint%20nem",
                    "a%20fenébe!%20nem.",
                    "persze%20miért%20ne",
                    "nem%20lmfao",
                    "persze,%20engem%20se%20érdekel%20jobban",
                    "Trump%20színe%20narancssárga?",
                    "én%20egy%208ball%20labda%20vagyok,%20nem%20foglalkozok%20a%20szar%20labdáiddal",
                    "biztos%20forrásból%20tudom:%20nem",
                    "biztos%20forrásból%20tudom:%20igen"
                ]
                # https://embed.rauf.wtf/?&author=%7B%7D&color=171A1B
                await dc.send(msg, "https://embed.rauf.wtf/?&author={}&color=171A1B".format(
                    lista8[
                        random.randrange(
                            len(lista8)
                        )
                    ]
                ))

        client.run(os.environ['BOT_TOKEN'])

    except Exception as e:
        print("\n\n")
        logging.error(f"Error code: {str(e)}")
        logging.info("Újraindítás...")
        continue
