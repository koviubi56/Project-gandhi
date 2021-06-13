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


async def main(msg, prefix: str) -> None:
    # PREFIXválassz ["asd", "dsa"]
    if len(msg.content) >= len(f"{prefix}válassz [\"1\", \"2\"]"):
        try:
            lista = list(msg.content[len(prefix) + len("válassz "):])
        except ValueError:
            await dc.send(msg, f"Szivatsz? Valami ilyesmit adjál má' meg: `{prefix}válassz [\"ez az első\", \"második\", \"3.\", \"minimum kettő dolognak kell lennie\", \"most már érted?!\"]`")
        else:
            await dc.send(msg, f"{choice(lista)}")
    else:
        await dc.send(
            msg, f"*Te sivatagi holló fejű sivatagi rák!* \nOszt mibő' válasszak? He?! \nValami ilyemi: `{prefix}válassz [\"Én nagyon \", \"szeretem a \", \"tejet\"]`")
