"""
File for "kép" command.
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

from random import choice
from discord_components import DiscordComponents, Button
from functools import lru_cache
import aiohttp
from asyncio import sleep

class MyErros:
    class StatusCodeError(Exception):
        pass

async def get_reddit(subreddit, listing, limit, timeframe):
    base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url) as r:
            if r.status < 400:  # OK
                return await r.json()
            raise MyErrors.StatusCodeError("r.status is {}".format(str(r.status)))

def myfind(inWhat: str, forWhat: tuple):
    for j in forWhat:
        if inWhat.find(j) != -1:
            return True
    return False

async def getText(what: str) -> str:
    cuteSubs = [
        "aww",
        "Eyebleach",
        "Blep",
        "brushybrushy",
        "catpictures",
        "AnimalsBeingBros"
    ]
    # MAX várakozás
    # SLEEPTIME | Sec
    # --------- | ---
    # 0.02      | 1
    # 0.04      | 2
    # 0.055     | 2.75
    # COMPONENT-NEK
    # 3 MP-EN BELÜL
    # VÁLASZOLNIA KELL
    SLEEPTIME = 0.055
    for x in range(50):
        try:
            global r
            r = await get_reddit(choice(cuteSubs) if what == "cute" else "shiba", "random", "1", "day")
            try:
                url = r[0]["data"]["children"][0]["data"]["secure_media"]["reddit_video"]["fallback_url"]
            except TypeError:
                url = r[0]["data"]["children"][0]["data"]["url_overridden_by_dest"]
            except KeyError:
                try:
                    url = r[0]["data"]["children"][0]["data"]["secure_media"]["oembed"]["url"]
                except KeyError:
                    url = r[0]["data"]["children"][0]["data"]["secure_media"]["oembed"]["thumbnail_url"]
            if myfind(url, ("gallery", "people.com")):
                sleep(SLEEPTIME)
                continue
        except Exception:
            sleep(SLEEPTIME)
            continue
        else:
            sub = r[0]["data"]["children"][0]["data"]["subreddit_name_prefixed"]
            tries = x + 1
            break
    else:
        return "**HIBA!** 50-szer próbálkoztunk, de nem találnunk egy képet. *Sad Gamdhi noises*"
    return f"{url} `({sub} | {tries})`"

@lru_cache
def comp(s1: int, s2: int, d1=False, d2=False):
    return [[Button(label="Cuki", id="kepCute", style=s1, disabled=d1), Button(label="Shiba", id="kepShiba", style=s2, disabled=d2)]]

async def main(msg, prefix, client):
    async def kuld():
        i = await client.wait_for("button_click", check=lambda i: i.component.id.startswith("kep"))
        if i.responded:
            return
        iid = i.component.id
        try:
            if iid == "kepCute":
                await i.respond(content=await getText("cute"), components=comp(s1=1, s2=2))
            elif iid == "kepShiba":
                await i.respond(content=await getText("shiba"), components=comp(s1=2, s2=1))
        except MyErrors.StatusCodeError as e:
            await i.respond("**Hiba!** `({})`".format(e))
        await kuld()


    global c
    c = client
    DiscordComponents(c)
    await msg.reply("Mit akarsz?", components=[[Button(label="Cuki", id="kepCute"), Button(label="Shiba", id="kepShiba")]])
    await kuld()
