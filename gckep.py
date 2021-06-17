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

import dc
from random import choice, randint

lastId = 0
reportok = []


def getText(what: str, prefix: str) -> str:
    if what.lower() == "cute":
        listUn = [
            "https://source.unsplash.com/collection/1489913",
            "https://source.unsplash.com/collection/992002",
            "https://source.unsplash.com/collection/3473478",
            "https://source.unsplash.com/collection/1758079",
            "https://source.unsplash.com/collection/307400",
            "https://source.unsplash.com/collection/9278231",
            "https://source.unsplash.com/collection/8514212",
            "https://source.unsplash.com/collection/4408740",
            "https://source.unsplash.com/collection/9251157",
            "https://source.unsplash.com/collection/17935256",
            "https://source.unsplash.com/collection/85013168",
            "https://source.unsplash.com/collection/1444235",
            "https://source.unsplash.com/collection/5058951",
            "https://source.unsplash.com/collection/8571458",
            "https://source.unsplash.com/collection/805851",
            "https://source.unsplash.com/collection/72016433",
            "https://source.unsplash.com/collection/4356106",
            "https://source.unsplash.com/collection/178050",
            "https://source.unsplash.com/collection/3657124",
            "https://source.unsplash.com/collection/8596141",
            "https://source.unsplash.com/collection/584209",
            "https://source.unsplash.com/collection/312000",
            "https://source.unsplash.com/collection/1244701",
            "https://source.unsplash.com/collection/8466901",
            "https://source.unsplash.com/collection/1291369",
            "https://source.unsplash.com/collection/976731",
            "https://source.unsplash.com/collection/17823258",
            "https://source.unsplash.com/collection/3226124",
            "https://source.unsplash.com/collection/2204857",
            "https://source.unsplash.com/collection/11381651",
            "https://source.unsplash.com/collection/4488725",
            "https://source.unsplash.com/collection/4558113",
            "https://source.unsplash.com/collection/2271561",
            "https://source.unsplash.com/collection/60923096",
            "https://source.unsplash.com/collection/8263951",
            "https://source.unsplash.com/collection/3143613",
            "https://source.unsplash.com/collection/3661977",
            "https://source.unsplash.com/collection/2270089",
            "https://source.unsplash.com/collection/11353054",
            "https://source.unsplash.com/collection/53728454",
            "https://source.unsplash.com/collection/1489292",
            "https://source.unsplash.com/collection/97648588",
            "https://source.unsplash.com/collection/2034865",
            "https://source.unsplash.com/collection/2047596",
            "https://source.unsplash.com/collection/2298069",
            "https://source.unsplash.com/collection/LDQLyupZ4YE",
            "https://source.unsplash.com/collection/8981289",
            "https://source.unsplash.com/collection/8658440",
            "https://source.unsplash.com/collection/4966708",
            "https://source.unsplash.com/collection/9290561",
            "https://source.unsplash.com/collection/228402",
            "https://source.unsplash.com/collection/23517384",
            "https://source.unsplash.com/collection/4635928",
            "https://source.unsplash.com/collection/8781437",
            "https://source.unsplash.com/collection/9451935",
            "https://source.unsplash.com/collection/1131206",
            "https://source.unsplash.com/collection/6797651",
            "https://source.unsplash.com/collection/2558692",
            "https://source.unsplash.com/collection/8242570",
            "https://source.unsplash.com/collection/1072946",
            "https://source.unsplash.com/collection/4992797",
            "https://source.unsplash.com/collection/9617498",
            "https://source.unsplash.com/collection/8297227",
            "https://source.unsplash.com/collection/949734"
        ]
        if randint(0, 2) != 0:
            import requests

            def get_reddit(subreddit, listing, limit, timeframe):
                base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
                request = requests.get(base_url, headers={
                    'User-agent': 'yourbot'})
                return request.json()
            while True:
                try:
                    global r
                    r = get_reddit("aww", "random", "1", "hour")
                    try:
                        url = r[0]["data"]["children"][0]["data"]["secure_media"]["reddit_video"]["fallback_url"]
                    except TypeError:
                        url = r[0]["data"]["children"][0]["data"]["url_overridden_by_dest"]
                    except KeyError:
                        try:
                            url = r[0]["data"]["children"][0]["data"]["secure_media"]["oembed"]["url"]
                        except KeyError:
                            url = r[0]["data"]["children"][0]["data"]["secure_media"]["oembed"]["thumbnail_url"]
                    id = "{}".format(r[0]["data"]["children"]
                                     [0]["data"]["subreddit_name_prefixed"])
                except Exception:
                    continue
                else:
                    break
        else:
            url = choice(listUn)
            id = f"unsplash/cute/{url[38:]}"
        global lastId
        lastId = id
        return f"{url} (`{prefix}kép report` | *{id}*)"
    elif what == "shiba":
        import requests

        def get_reddit(subreddit, listing, limit, timeframe):
            base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
            request = requests.get(base_url, headers={
                'User-agent': 'yourbot'})
            return request.json()
        while True:
            try:
                #global r
                r = get_reddit("shiba", "random", "1", "hour")
                try:
                    url = r[0]["data"]["children"][0]["data"]["secure_media"]["reddit_video"]["fallback_url"]
                except TypeError:
                    url = r[0]["data"]["children"][0]["data"]["url_overridden_by_dest"]
                except KeyError:
                    try:
                        url = r[0]["data"]["children"][0]["data"]["secure_media"]["oembed"]["url"]
                    except KeyError:
                        url = r[0]["data"]["children"][0]["data"]["secure_media"]["oembed"]["thumbnail_url"]
                id = "{}".format(r[0]["data"]["children"][0]
                                 ["data"]["subreddit_name_prefixed"])
            except Exception:
                continue
            else:
                break
        #global lastId
        lastId = id
        return f"{url} (`{prefix}kép report` | *{id}*)"
    elif what.startswith("r/") or what.startswith("toph/r/") or what.startswith("topd/r/"):
        if what.startswith("r/"):
            what = what[len("r/"):]
        elif what.startswith("toph/r/"):
            what = what[len("toph/r/"):]
        elif what.startswith("topd/r/"):
            what = what[len("topd/r/"):]

        import requests

        def get_reddit(subreddit, listing, limit, timeframe):
            base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
            request = requests.get(base_url, headers={
                'User-agent': 'yourbot'})
            return request.json()
        while True:
            try:
                #global r
                if what.startswith("r/"):
                    r = get_reddit(what, "random", "1", "hour")
                elif what.startswith("toph/r/"):
                    r = get_reddit(what, "top", "1", "hour")
                elif what.startswith("topd/r/"):
                    r = get_reddit(what, "top", "1", "day")

                try:
                    url = r[0]["data"]["children"][0]["data"]["secure_media"]["reddit_video"]["fallback_url"]
                except TypeError:
                    url = r[0]["data"]["children"][0]["data"]["url_overridden_by_dest"]
                except KeyError:
                    try:
                        url = r[0]["data"]["children"][0]["data"]["secure_media"]["oembed"]["url"]
                    except KeyError:
                        url = r[0]["data"]["children"][0]["data"]["secure_media"]["oembed"]["thumbnail_url"]
                id = "{}".format(r[0]["data"]["children"][0]
                                 ["data"]["subreddit_name_prefixed"])
            except Exception:
                continue
            else:
                break
        #global lastId
        lastId = id
        return f"{url} (`{prefix}kép report` | *{id}*)"
    else:
        raise ValueError("{} is not in this list: {}".format(
            what, str(["cute", "shiba"])))


async def main(msg, prefix):
    # PREFIXkép [äđĐ]
    if len(msg.content) > len(f"{prefix}kép "):
        kwd = msg.content[len(f"{prefix}kép "):]
        if kwd == "cute":
            await dc.send(msg, getText("cute", prefix))
        elif kwd == "shiba":
            await dc.send(msg, getText("shiba", prefix))

        elif kwd == "report":
            global lastId
            reportok.append({"id": lastId, "bejelento": str(msg.author)})
            import time
            with open(f"report-{str(time.time())}.json", "+") as f:
                f.write(str(reportok))
            await dc.send(msg, f"```py\n{reportok}\n```")
        elif kwd.startswith("r/") or kwd.startswith("toph/r/") or kwd.startswith("topd/r/"):
            await dc.send(msg, getText(kwd, prefix))
        else:
            id = f"unsplash/custom/{kwd}"
            await dc.send(msg, f"https://source.unsplash.com/featured/?{kwd} (*{id}*)")
    else:
        await dc.send(msg, "EEEEEEE! Oszt mit mutassak?!")
