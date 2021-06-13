"""
File for "válassz" command.
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
from random import choice

lastId = 0
reportok = []


def getText(prefix: str) -> str:
    url = choice([
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
        "https://source.unsplash.com/collection/949734"
    ])
    id = url[38:]
    lastId = id
    return f"{url} (`{prefix}kép report` | *{id}*)"


async def main(msg, prefix):
    # PREFIXkép [äđĐ]
    if len(msg.content) > len(f"{prefix}kép "):
        if msg.content[len(f"{prefix}kép "):] == "cute":
            await dc.send(msg, getText(prefix))
        elif msg.content[len(f"{prefix}kép "):] == "report":
            reportok.append({"id": lastId, "bejelento": str(msg.author)})
            await dc.send(msg, f"```py\n{reportok}\n```")
    else:
        await dc.send(msg, "EEEEEEE! Oszt mit mutassak?!")
