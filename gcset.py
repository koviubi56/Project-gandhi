"""
File for "set" command.
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

import logging
logging = logging.getLogger(__name__)


async def main(content, prefix):
    logging.warning(
        "Valaki meg akarja változtatni a szerdák számát! Infókat lásd alább:")
    if len(content) > len(prefix) + len("set "):
        with open("db.txt", "w") as f:
            f.write(str(int(content[len(prefix) + len("set "):])))
