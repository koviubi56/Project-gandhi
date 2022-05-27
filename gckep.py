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

from random import choice, randint
from discord_components import DiscordComponents, Button
from functools import lru_cache
from asyncio import sleep
from asyncio import run as asyncrun
from secrets import token_urlsafe
import aiohttp
import textwrap
from threading import Thread


class MyErrors:
    class StatusCodeError(Exception):
        pass


async def www_get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            return r


async def get_reddit(subreddit, listing, limit, timeframe):
    base_url = f"https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}"
    async with aiohttp.ClientSession() as session:
        async with session.get(
            base_url, headers={"User-agent": token_urlsafe()}
        ) as r:
            with open("output.txt", "w") as f:
                f.write(await r.text())
            if r.status < 400:  # OK
                return await r.json()
            raise MyErrors.StatusCodeError(r.status)


@lru_cache
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
        "AnimalsBeingBros",
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
    SLEEPTIME = 0.02
    for x in range(20):
        try:
            if (
                what == "shiba"
                or choice(("REDDIT", "API")) == "REDDIT"
            ):
                global r
                r = await get_reddit(
                    choice(cuteSubs) if what == "cute" else "shiba",
                    "random",
                    "1",
                    "day",
                )
                # return f"Debug: {r = }"
                try:
                    url = r[0]["data"]["children"][0]["data"][
                        "secure_media"
                    ]["reddit_video"]["fallback_url"]
                except TypeError:
                    url = r[0]["data"]["children"][0]["data"][
                        "url_overridden_by_dest"
                    ]
                except KeyError:
                    try:
                        url = r[0]["data"]["children"][0]["data"][
                            "secure_media"
                        ]["oembed"]["url"]
                    except KeyError:
                        url = r[0]["data"]["children"][0]["data"][
                            "secure_media"
                        ]["oembed"]["thumbnail_url"]
                if myfind(url, ("gallery", "people.com", "bbc")):
                    await sleep(SLEEPTIME)
                    continue
            else:

                async def __():
                    global url
                    if randint(1, 2) == 1:
                        url = choice(
                            (
                                f"http://placekitten.com/{randint(20, 4000)}/{randint(20, 4000)}",
                                f"https://randomfox.ca/images/{randint(1, 123)}.jpg",
                            )
                        )
                    else:
                        url = await www_get(
                            "https://aws.random.cat/meow"
                        )
                        url = await url.json()
                        url = url["json"]
                    if not (r := await www_get(url)).ok:
                        raise MyErrors.StatusCodeError(r.status)

                t = Thread(target=lambda: asyncrun(__()))
                t.start()
                t.join(timeout=SLEEPTIME)
                if t.is_alive():
                    raise TimeoutError("-1; thread timed out")
        except MyErrors.StatusCodeError as e:
            print("[ERROR] StatusCodeError:", e)
            await sleep(SLEEPTIME)
            continue
        except TimeoutError as e:
            print("[ERROR] TimeoutError:", e)
            continue
        except Exception:
            from traceback import print_exc

            print_exc()
            await sleep(SLEEPTIME)
            continue
        else:
            try:
                sub = r[0]["data"]["children"][0]["data"][
                    "subreddit_name_prefixed"
                ]
            except (NameError, UnboundLocalError):
                pass
            tries = x + 1
            break
    else:
        return "**HIBA!** 20-szor próbálkoztunk, de nem találnunk egy képet se. *Sad Gamdhi noises*"
    try:
        return f"{url} `({sub} | {tries})`"
    except UnboundLocalError:
        return await getText(what)


@lru_cache
def comp(s1: int, s2: int, d1=False, d2=False):
    return [
        [
            Button(label="Cuki", id="kepCute", style=s1, disabled=d1),
            Button(
                label="Shiba", id="kepShiba", style=s2, disabled=d2
            ),
        ]
    ]


async def main(msg, prefix, client):
    # msg.reply("429")
    # return 1
    async def kuld():
        i = await client.wait_for(
            "button_click",
            check=lambda i: i.component.id.startswith("kep"),
        )
        with msg.channel.typing():
            if i.responded:
                return
            iid = i.component.id
            try:
                if iid == "kepCute":
                    await i.respond(
                        content=await getText("cute"),
                        components=comp(s1=1, s2=2),
                    )
                elif iid == "kepShiba":
                    await i.respond(
                        content=await getText("shiba"),
                        components=comp(s1=2, s2=1),
                    )
            except MyErrors.StatusCodeError as e:
                await i.respond(f"**Hiba!** `({hash(e)})`")
        await kuld()

    global c
    c = client
    DiscordComponents(c)
    await msg.reply(
        "Mit akarsz?",
        components=[
            [
                Button(label="Cuki", id="kepCute"),
                Button(label="Shiba", id="kepShiba"),
            ]
        ],
    )
    await kuld()
