# -*- coding: utf-8 -*-
# coding: utf-8
print("========================GANDHI BOT 1.0.0=======================")
# ===SETTINGS===
maxSzerda = 255 # Mennyi a maximális szerda amennyit elfogad egy üzenethez.
# ---SETTINGS---

if type(maxSzerda) is not int:
    raise TypeError(f"BY ME: A maxSzerda nem int, hanem {type(maxSzerda)}")

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
import discord # 1
from replit import db # 2
import getpass # 3
import random
import os # 4

client = discord.Client() # 5

@client.event
async def on_ready():
    print("""THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.""")
    print('Bejelentkezve: "{0.user}"'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    plus = 0
    msg = message.content.lower()

    try:
        for i, betu in enumerate(msg):
            if betu.lower() == "s":
                if msg[i + 1] == "z":
                    if msg[i + 2] == "e":
                        if msg[i + 3] == "r":
                            if msg[i + 4] == "d":
                                if msg[i + 5] == "a":
                                    plus += 1
                                    continue
            if plus > maxSzerda:
                print("TÚL SOK SZERDA!")
                await message.channel.send(f"Ez az üzenet annyira menő, hogy több mint {maxSzerda} szerda van benne.")
                plus = int(input("Mennyi szerda legyen: "))
                break

            continue
    except IndexError:
        pass
    
    if plus > 0:
        db["szerdak"] += plus
        await message.channel.send(f"+{plus} szerda")

    if msg.startswith('56'):
        await message.channel.send('Szerdák száma: ' + str(db["szerdak"]))
    
    if msg.startswith('admin.projectgandhi'):
        pwdDC = random.randrange(100000, 1000000)
        await message.channel.send(f"|| {pwdDC} ||")
        pwdC = int(getpass.getpass("Password Discord: "))
        if pwdC == pwdDC:
            pwdC2 = getpass.getpass("Password console: ")
            if pwdC2 == os.environ['KEY']:
                db["szerdak"] = 0
                print("Yes")
            else:
                print("No2")
        else:
            print("No1")

client.run(os.environ['BOT_TOKEN'])