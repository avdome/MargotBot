import asyncio

import discord
import os

from Code.Handlers import *
from Commands import *

client = discord.Client()


@client.event
async def on_ready() -> None:  # printed in terminal when bot is ready to be used
    print('Hello I am {0.user}.'.format(client))


@client.event
async def on_message(msg: Message) -> None:
    cmd = handler_starter(msg)

    if cmd:  # Makes sure cmd is not None.
        cmd.execute()


def handler_starter(msg: Message) -> Optional[Command]:
    """
    Runs through the handlers and returns a Command from them. Unless the
    message cannot be handled, in which case it will return None.
    """

    music = MusicHandler()
    roller = RollingHandler()

    music.set_next(roller)

    return music.Handle(msg)
