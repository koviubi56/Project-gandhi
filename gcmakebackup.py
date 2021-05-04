"""
File for the "makebackup" command.
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
import time
from replit import db
import dc
import logging
logging = logging.getLogger(__name__)


async def main(msg):
    logging.warning(
        "\"{}\" szeretne csinálni egy biztonsági mentést! Infókat lásd alább:".format(msg.author))
    print("MOST:szerdak = \"{szerda}\"; backup = \"{bu}\"".format(
        szerda=db["szerdak"], bu=db["backup"]))
    BUlesz = db["backup"]
    BUlesz["CMDbackup"] = {
        "szerdak": db["szerdak"],
        "time": time.asctime()
    }
    print("LESZ: backup = \"{}\"".format(str(BUlesz)))
    dc.backup("CMD")
    logging.info("Backup kész!")
    await dc.send(msg, "Backup kész!")
