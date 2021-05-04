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
        # ===GC===
        import gchjelp
        import gfindszerda
        import gc56
        import gcstop
        import gcset
        import gcmakebackup
        import gcresetbackup
        import gcgetbackup
        import gc8ball
        import gcbolcsesseg
        # ---GC---
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

        @client.event
        async def on_ready():
            await client.change_presence(activity=discord.Game("Szőr"), status=discord.Status.online)
            print("-----")
            print("This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.")

            logging.info('Bejelentkezve: "{0.user}"'.format(client))

            dc.backup("AUTO")

        @client.event
        async def on_message(message):
            if message.author == client.user:
                return

            time.sleep(0.1)

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
                gchjelp.main(msg, prefix)

            # szerda keresés
            gfindszerda.main(msg, maxSzerda)

            # 56
            if content == "56":
                gc56.main(msg)

            # stop
            if dc.cmd(msg, os.environ["KEY"], [
                ["stop", True]
            ]):
                gcstop.main(msg)

            # set
            if dc.cmd(msg, os.environ["KEY"], [
                ["set", True]
            ]):
                gcset.main(content, prefix)

            # makeBackup
            if dc.cmd(msg, os.environ["KEY"], [
                ["makebackup", True]
            ]):
                gcmakebackup.main(msg)

            # resetBackup
            if dc.cmd(msg, os.environ["KEY"], [
                ["resetbackup", True]
            ]):
                gcresetbackup.main(msg)


            # getBackup
            if dc.cmd(msg, prefix, [
                ["getbackup", True]
            ]):
                gcgetbackup.main(msg)

            # 8ball
            if dc.cmd(msg, prefix, [
                ["8ball", True]
            ]):
                gc8ball.main(msg, prefix)


            # bölcsesség
            if dc.cmd(msg, prefix, [
                ["bölcsesség", True],
                ["bolcsesseg", True],
                ["idézet", True],
                ["idezet", True],
                ["quote", True]
            ]):
                gcbolcsesseg.main(msg)


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
                if len(msg.content) <= len(prefix) + len("gtn") + 1:
                    await dc.send(msg, "Mennyi legyen a max szám? He?!")
                    await dc.send(msg, f"Így használd: `{prefix}gtn `*<MAX SZÁM>*")
                    await dc.send(msg, f"PL: `{prefix}gtn 756`")
                else:
                    gtNum = random.randrange(
                        1, int(msg.content[len(prefix) + 4:]))
                    inGtn = True
                    await dc.send(msg, "A nyeremény a lottó számok. Hajrá!")

        client.run(os.environ["BOT_TOKEN"])

    except Exception as e:
        print("\n\n[ERROR]")
        print(f"Error code: \"{str(e)}\"")
        print("Újraindítás...")
        continue
