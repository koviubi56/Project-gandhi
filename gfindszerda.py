"""
This file is for finding "szerda"s in messages.
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
import logging
logging = logging.getLogger(__name__)


async def main(msg, maxSzerda):
    content = msg.content
    plus = 0
    try:
        for i, betu in enumerate(content):
            if plus > maxSzerda:
                logging.error("TÚL SOK SZERDA!")
                await dc.send(
                    msg, f"Ez az üzenet annyira menő, hogy több mint {maxSzerda} szerda van benne.")
                await dc.send(msg, "|| Megjegyzés magamnak: *set* ||")
                plus = 0
                break
            if (
                betu.lower() == "s"
                and content[i + 1] == "z"
                and content[i + 2] == "e"
                and content[i + 3] == "r"
                and content[i + 4] == "d"
                and content[i + 5] in ["a", "á"]
            ):
                plus += 1
            continue
    except IndexError:
        pass

    if plus > 0:
        with open("db.txt", "w+") as f:
            print(
            f"DEBUG: [2] f = {f}; f.readable = {f.readable()}; f.read = {f.read()}; f.readline = {f.readline()}; f.readlineS = {f.readlines}")
            f.write(str(int(f.read()) + plus))
            print("DEBUG: [1] {}".format(str(f.readable())))
            await dc.send(msg, "+{plus} szerda (most: {szerdak})".format(plus=plus, szerdak=f.read()))
