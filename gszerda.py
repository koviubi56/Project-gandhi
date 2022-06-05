from asyncio import run, sleep
import datetime
import functools
import threading
import discord

CHANNEL_ID = 694513594016071711  # REAL
CEST = datetime.timezone(datetime.timedelta(hours=2), "CEST")
CET = datetime.timezone(datetime.timedelta(hours=1), "CET")

CURRENT = CEST


def szerda_file() -> str:
    with open("szerda.txt", encoding="utf-8") as f:
        return f.read()


def update_szerda_file() -> int:
    with open("szerda.txt", "w", encoding="utf-8") as f:
        return f.write(str(last_szerda().timestamp()))


def last_szerda() -> datetime.datetime:
    # Get the last wednesday
    rv = datetime.datetime.now(CURRENT)
    while True:
        if rv.weekday() == 2:
            rv = datetime.datetime(
                year=rv.year, month=rv.month, day=rv.day, hour=3
            )
            break
        rv -= datetime.timedelta(days=1)
    print(f"last szerda {rv}")
    return rv


def is_new_szerda_needed() -> bool:
    return (
        datetime.datetime.fromtimestamp(float(szerda_file())) < last_szerda()
    )


async def if_new_szerda_is_needed_send_msg(
    client: discord.Client,
) -> bool:
    if not is_new_szerda_needed():
        print("no new szerda")
        return False
    print("new szerda😃😃")
    print(client._connection.guilds)
    channel: discord.TextChannel = client.get_channel(CHANNEL_ID)
    assert channel, f"{channel=!r}"
    msg: discord.Message = await channel.send(
        "@everyone https://cdn.discordapp.com/attachments/711248172122505266"
        "/897876969985835008/dudes.webm"
    )
    await msg.add_reaction("frog")
    update_szerda_file()
    return True


async def loop(client: discord.Client) -> None:
    print(f"loop called with {client=!r}")
    while True:
        print("new iter")
        print("if new do")
        await if_new_szerda_is_needed_send_msg(client)
        print("sleep")
        await sleep(60)
