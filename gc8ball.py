"""
This file is for the "8ball" command.
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

import discord
import random
import dc


async def main(msg, prefix):
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
