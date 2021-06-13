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

while True:
    print("Starting...")
    try:
        import os
        import discord
        import random
        import dc
        import time
        import ddos
        # ===GC===
        import gchjelp
        import gfindszerda
        import gc56
        import gcset
        import gc8ball
        import gcbolcsesseg
        import gcvalassz
        import gckep
        # ---GC---
        with open("db.txt") as f:
            print("szerdak = \"{szerdak}\"; type(szerdak) = \"{szerdakT}\"".format(
                szerdak=str(f.read()),
                szerdakT=str(type(f.read()))
            ))

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
        pre = "-beta.3"
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

        @client.event
        async def on_ready():
            await client.change_presence(activity=discord.Game("Szőr"), status=discord.Status.online)
            print("-----")
            print("This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.")

            logging.info('Bejelentkezve: "{0.user}"'.format(client))

        @client.event
        async def on_message(message):
            if message.author == client.user:
                return

            time.sleep(0.1)

            d = ddos.DDoS(3, 7, 5, 15)
            if d.test(message.author):
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
                    await gchjelp.main(msg, prefix)

                # szerda keresés
                await gfindszerda.main(msg, maxSzerda)

                # 56
                if content == "56":
                    await gc56.main(msg)

                # set
                if dc.cmd(msg, os.environ["KEY"], [
                    ["set", True]
                ]):
                    await gcset.main(content, os.environ["KEY"])

                # 8ball
                if dc.cmd(msg, prefix, [
                    ["8ball", True]
                ]):
                    await gc8ball.main(msg, prefix)

                # bölcsesség
                if dc.cmd(msg, prefix, [
                    ["bölcsesség", True],
                    ["bolcsesseg", True],
                    ["idézet", True],
                    ["idezet", True],
                    ["quote", True]
                ]):
                    await gcbolcsesseg.main(msg)

                # válassz
                if dc.cmd(msg, prefix, [
                    ["válassz", True],
                    ["valassz", True]
                ]):
                    await gcvalassz.main(msg, prefix)

                # kép
                if dc.cmd(msg, prefix, [
                    ["kép", True],
                    ["kep", True]
                ]):
                    await gckep.main(msg, prefix)

                # *************************************************************************************

                # kagi
                if dc.cmd(msg, prefix, [
                    ["kagi", True],
                    ["kaga", True]
                ]):
                    await dc.send(msg, ":poop:")

                # bajsz
                if dc.cmd(msg, prefix, [
                    ["bajsz", True]
                ]):
                    bajszLista = [
                        ":disguised_face:",
                        ":man:",
                        ":bearded_person:",
                        ":santa:"
                    ]
                    await dc.send(msg, random.choice(bajszLista))

                # gtn
                global inGtn
                if inGtn:
                    global gtNum
                    if msg.content == "__gtn:end__":
                        inGtn = False
                    else:
                        if int(content) == int(gtNum):
                            inGtn = False
                            await dc.send(msg, "Jippí!")
                            await dc.send(msg, "Lottószámok (ötös lottó): || {} {} {} {} {} ||".format(random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46), random.randrange(1, 46)))
                        elif int(content) > int(gtNum):
                            await dc.send(msg, "Kisebb!")
                        elif int(content) < int(gtNum):
                            await dc.send(msg, "Nagyobb!")

                if dc.cmd(msg, prefix, [
                    ["gtn", True]
                ]):
                    # beírt egyáltalán valamit?
                    if len(msg.content) <= len(prefix) + len("gtn") + 1:
                        await dc.send(msg, "Mennyi legyen a max szám? He?!")
                        await dc.send(msg, f"Így használd: `{prefix}gtn `*<MAX SZÁM>*")
                        await dc.send(msg, f"PL: `{prefix}gtn 756`")
                    else:
                        # számot írt be?
                        try:
                            _ = int(msg.content[len(prefix) + len("gtn "):])
                        except Exception as e:
                            logging.error("Nem sikerült a konvertálás!")
                            print(f"Hiba kód: {e}")
                            print("Amivel próbálkoztunk: {}; típusa: {}".format(msg.content[len(
                                prefix) + len("gtn "):], type(msg.content[len(prefix) + len("gtn "):])))
                            await dc.send(
                                msg, "Bocs, de valszeg (99,9%) amit beírtál az nem egy szám. Adj meg egy EGÉSZ számot, ami NAGYOBB mint 1, de KISEBB mint 2.147.483.647!")
                        else:
                            # egy int számot írt be ami 1<X<2.147.483.647 (2 MRD)
                            if int(msg.content[len(prefix) + len("gtn "):]) > 1 and int(msg.content[len(prefix) + len("gtn "):]) < 2_147_483_647:
                                gtNum = random.randrange(
                                    1, int(msg.content[len(prefix) + len("gtn "):]) + 1)
                                inGtn = True
                                await dc.send(msg, f"Van a billentyűteted. Írj be egy számot 1 és {msg.content[len(prefix) + 4:]} között. Nyomd meg az [ENTER] gombot. Visszakapod azt hogy `Kisebb!`, `Nagyobb!`, vagy azt hogy `Jippí!`. Most már érted?!\nIllusztráció: https://cdn.discordapp.com/attachments/741670562585247835/843095037079715930/unknown.png\n*A tájékoztatás nem teljeskörő. További infókért kérdezd meg anyádat.*")
                            else:
                                await dc.send(
                                    msg, "Bocs, de amit beírtál az nem okés. Adj meg egy EGÉSZ számot, ami NAGYOBB mint 1, de KISEBB mint 2.147.483.647!")

            else:
                time.sleep(1)

        client.run(os.environ["BOT_TOKEN"])

    except Exception as e:
        print("\n\n[ERROR]")
        print(f"Error code: \"{str(e)}\"")
        print("Újraindítás...")
        continue
