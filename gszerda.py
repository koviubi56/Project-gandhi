from asyncio import run, sleep
import datetime
import functools
import threading
import discord

CHANNEL_ID = 694513594016071711  # REAL


def date_to_datetime(date: datetime.date) -> datetime.datetime:
    return datetime.datetime.combine(date, datetime.time())


def szerda_file() -> str:
    with open("szerda.txt", encoding="utf-8") as f:
        return f.read()


def update_szerda_file() -> None:
    with open("szerda.txt", "w", encoding="utf-8") as f:
        f.write(str(int(date_to_datetime(last_szerda()).timestamp())))


def last_szerda() -> datetime.date:
    # Get the last wednesday
    rv = datetime.date.today()
    while True:
        if rv.weekday() == 2:
            break
        rv -= datetime.timedelta(days=1)
    return rv


def is_new_szerda_needed() -> bool:
    return (
        datetime.date.fromtimestamp(int(szerda_file()))
        < last_szerda()
    )


async def if_new_szerda_is_needed_send_msg(
    client: discord.Client,
) -> bool:
    if not is_new_szerda_needed():
        return False
    channel: discord.TextChannel = client.get_channel(CHANNEL_ID)
    await channel.send(
        "@everyone https://cdn.discordapp.com/attachments/711248172122505266"
        "/897876969985835008/dudes.webm"
    )
    update_szerda_file()


async def loop(client: discord.Client) -> None:
    while True:
        await if_new_szerda_is_needed_send_msg(client)
        await sleep(10)


def run_thread(client: discord.Client) -> None:
    return threading.Thread(
        target=functools.partial(run, loop(client))
    ).start()
