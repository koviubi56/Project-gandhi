"""
File for the "h(j)elp" command.
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
import random
import dc
import discord


async def main(msg, prefix):
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
    embedHjelp.add_field(
        name="bajsz",
        value=f":bearded_person:\n__Szintaxis__: `{prefix}bajsz`\n__PL__: `{prefix}bajsz`"
    )
    embedHjelp.add_field(
        name="bölcsesség",
        value=f"Egy veri szpesöl idézet Gandhi-tól (igen, :gandhi:)\n__Szintaxis__: `{prefix}bölcsesség`\n__PL__: `{prefix}bölcsesség`"
    )

    await dc.embed(msg, embedHjelp)
