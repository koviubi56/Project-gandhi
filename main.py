# -*- coding: utf-8 -*-
# coding: utf-8

"""
This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. 
If a copy of the MPL was not distributed with this file, 
You can obtain one at http://mozilla.org/MPL/2.0/.
"""

try:
    from replit import db
except Exception as e:
    print("[ERROR]")
    print(f"Error when importin db from replit: {str(e)}")
    print("Trying again...")
    for e2 in range(5):
        try:
            from replit import db
        except:
            if e2 < 4:
                print(f"[ERROR {e2} ]")
            elif e2 >= 4:
                print("*** CRITICAL ERROR! ***")
                print("We can't import db from replit after 6 tries.")
                print("The bot CAN'T work without it.")
                print("Stopping...")
                exit()
try:
    db["szerdak"] -= 1
except:
    db["szerdak"] = 0
else:
    db["szerdak"] += 1
finally:
    inSet = False

while True:
    print("Starting...")
    try:
        import os
        import discord
        import random
        import dc
        from logging import *
        import logging
        logging.basicConfig(level=logging.ERROR, format="[%(name)s %(asctime)s %(levelname)s line: %(lineno)d] %(message)s")
        # logging.basicConfig(level=logging.DEBUG, format="[%(name)s %(asctime)s %(levelname)s line: %(lineno)d] %(message)s")

        logging.info("Starting...")
        # ===SETTINGS===
        # Mennyi a maximális szerda amennyit elfogad egy üzenethez.
        maxSzerda = 510
        # Verzió
        version = "1.3.0"
        # Bármi más? "-beta.1"?
        pre = "-beta.2"
        # Prefix
        prefix = "56!"
        # ---SETTINGS---

        print('{:=^63}'.format(f'GANDHI BOT {version}{pre}'))

        client = discord.Client()

        @client.event
        async def on_ready():
            logging.basicConfig(level=logging.DEBUG, format="[%(name)s %(asctime)s %(levelname)s line: %(lineno)d] %(message)s")
            print('This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.')
            logging.debug('Bejelentkezve: "{0.user}"'.format(client))

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
                        print("TÚL SOK SZERDA!")
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
            if dc.cmd(os.environ['KEY'], 'stop', msg):
                await dc.send(msg, f'Szerdák: {str(db["szerdak"])}')
                print("Stopping...")
                exit()

            # set
            global inSet
            if inSet == True:
                inSet = False
                db["szerdak"] = content

            if dc.cmd(os.environ['KEY'], 'set', msg):
                await dc.send(msg, 'K!')
                inSet = True

            # 8ball
            if dc.cmd(prefix, "8ball", msg):
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
        print("[ERROR]")
        print(f"Error code: {str(e)}")
        print("Restarting...")
