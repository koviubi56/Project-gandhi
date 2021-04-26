# -*- coding: utf-8 -*-
# coding: utf-8

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
        print('{:=^63}'.format('GANDHI BOT 1.3.0-beta'))
        # ===SETTINGS===
        # Mennyi a maximális szerda amennyit elfogad egy üzenethez.
        maxSzerda = 255
        # ---SETTINGS---

        client = discord.Client()

        @client.event
        async def on_ready():
            print('This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.')
            print('Bejelentkezve: "{0.user}"'.format(client))

        @client.event
        async def on_message(message):
            if message.author == client.user:
                return

            plus = 0
            msg = message.content.lower()

            try:
                for i, betu in enumerate(msg):
                    if plus > maxSzerda:
                        print("TÚL SOK SZERDA!")
                        await message.channel.send(f"Ez az üzenet annyira menő, hogy több mint {maxSzerda} szerda van benne.")
                        await message.channel.send("f|| Megjegyzés magamnak: *set*; szerdák: {str(db[szerdak])} ||")
                        plus = 0
                        break
                    if betu.lower() == "s":
                        if msg[i + 1] == "z":
                            if msg[i + 2] == "e":
                                if msg[i + 3] == "r":
                                    if msg[i + 4] == "d":
                                        if msg[i + 5] == "a" or msg[i + 5] == "á":
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
                await message.channel.send(f"+{plus} szerda")

            if msg.startswith('56'):
                await message.channel.send(f'Szerdák száma: {str(db["szerdak"])}')

            if msg.startswith('admin.projectgandhi'):
                db["szerdak"] = 0

            if msg.startswith('stop.projectgandhi'):
                await message.channel.send(f'Szerdák: {str(db["szerdak"])}')
                print("Stopping...")
                exit()

            global inSet
            if inSet == True:
                inSet = False
                db["szerdak"] = msg

            if msg.startswith('set.projectgandhi'):
                await message.channel.send('K!')
                inSet = True

        client.run(os.environ['BOT_TOKEN'])
    except Exception as e:
        print("\n\n")
        print("[ERROR]")
        print(f"Error code: {str(e)}")
        print("Restarting...")
