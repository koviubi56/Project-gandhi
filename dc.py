"""
Functions for Discord messages.
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

import discord
import logging
logging = logging.getLogger(__name__)


async def send(msg, text):
    """Send a message

    Args:
        msg (dict): The message that discord gave
        text (str): The text. It can be "this"; or f"this {x}"; or "this {}".format("x")
    """
    try:
        await msg.channel.send(text)
    except Exception as e:
        logging.error("[ERROR] " + str(e))
    else:
        logging.info("Üzenet elküldve! (CH: \"{ch}\"; MSG: \"{msg}\")".format(
            ch=msg.channel, msg=text))


async def embed(msg, embedVar):
    """Send an embed message

    Args:
        msg (dict): The message that discord gave
        embedVar (???): The embed variable
    """
    try:
        await msg.channel.send(embed=embedVar)
    except Exception as e:
        logging.error(str(e))
    else:
        logging.info("Embed elküldve! (CH: \"{}\")".format(msg.channel))


def cmd(msg, prefix, command):
    """Checks if the msg is a command

    Args:
        prefix (str): The prefix
        command (str): The command
        msg (disct): The message that discord gave

    Returns:
        [type]: [description]
    """
    if msg.content.lower().startswith(prefix.lower() + command.lower()):
        return True
    # // else:
    return False
