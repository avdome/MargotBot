import os
from typing import Optional
import discord
from discord import Message
from Handlers import MusicHandler, RollingHandler, GeneralHandler
from Commands import Command

client = discord.Client()

# Constant that indicates a command in discord
INDICATOR_CONSTANT = '!'


# printed in terminal when bot is ready to be used
@client.event
async def on_ready() -> None:
    print('Hello I am {0.user}.'.format(client))


@client.event
async def on_message(msg: Message) -> None:

    if bot_author(msg):
        return None

    # Determine if the indicator is in the message.
    if msg.content.startswith(INDICATOR_CONSTANT):
        msg.content = msg.content[1:].lower()
        cmd = handler_starter(msg)
    else:
        cmd = None

    if cmd:  # Makes sure cmd is not None.
        cmd.execute()


def handler_starter(msg: Message) -> Optional[Command]:
    """
    Runs through the handlers and returns a Command from them. Unless the
    message cannot be handled, in which case it will return None.
    """

    music = MusicHandler()
    roller = RollingHandler()
    general = GeneralHandler()

    music.set_next(roller)
    roller.set_next(general)

    return music.Handle(msg)


def bot_author(msg: Message) -> bool:
    """ Returns True if the author of the Message is the bot and False
    otherwise. """

    if msg.author == client.user:
        return True
    return False


client.run(os.environ['TOKEN'])



