"""
This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. 
If a copy of the MPL was not distributed with this file, 
You can obtain one at http://mozilla.org/MPL/2.0/.
"""

import discord


def send(msg, text):
    """Send a message

    Args:
        msg (dict): The message that discord gave
        text (str): The text. It can be "this"; or f"this {x}"; or "this {}".format("x")
    """
    msg.channel.send(text)


def cmd(prefix, command, msg):
    """Checks if the msg is a command

    Args:
        prefix (str): The prefix
        command (str): The command
        msg (disct): The message that discord gave

    Returns:
        [type]: [description]
    """
    if msg.content.startswith(prefix + command):
        return True
    # // else:
    return False