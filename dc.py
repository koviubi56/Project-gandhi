"""
This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. 
If a copy of the MPL was not distributed with this file, 
You can obtain one at http://mozilla.org/MPL/2.0/.
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
        logging.error(str(e))
    else:
        logging.info("Üzenet elküldve! (CH: {ch}; MSG: {msg})".format(
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
        logging.info("Embed elküldve! (CH: {})".format(msg.channel))


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