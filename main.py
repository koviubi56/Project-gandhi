# -*- coding: utf-8 -*-
# coding: utf-8

try:
    from replit import db
except Exception as e:
    print("[ERROR]")
    print("Error when importin db from replit: " + str(e))
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
    if db["szerdak"] < 1:
        db["szerdak"] = 0
finally:
    inSet = False

while True:
    print("Starting...")
    try:
        import os
        import discord
        print("========================GANDHI BOT 1.1.0=======================")
        # ===SETTINGS===
        # Mennyi a maximális szerda amennyit elfogad egy üzenethez.
        maxSzerda = 255
        # ---SETTINGS---

        """
        ISC License
        Copyright (c) Koviubi56 (koviubi#4465)
        Permission to use, copy, modify, and/or distribute this software for any
        purpose with or without fee is hereby granted, provided that the above
        copyright notice and this permission notice appear in all copies.
        THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
        WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
        MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
        ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
        WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
        ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
        OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
        """

        client = discord.Client()

        @client.event
        async def on_ready():
            print('THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.')
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
                        plus = maxSzerda + 1
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
                await message.channel.send('Szerdák száma: ' + str(db["szerdak"]))

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
        print("Error code: " + str(e))
        print("Restarting...")