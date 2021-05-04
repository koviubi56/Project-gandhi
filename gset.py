"""
File for setting the szerdas.
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
# * **************************** *
# * This is NOT for the command! *
# * This is for the setting!     *
# * **************************** *

from replit import db
import logging
logging = logging.getLogger(__name__)


def main(inSet, content):
    if inSet == True:
        inSet = False
        db["szerdak"] = int(content)
        logging.info("Szerda beállítva! Mostani szerda: \"{most}\"  Backup: \"{bu}\"".format(
            most=db["szerdak"], bu=str(db["backup"])))
