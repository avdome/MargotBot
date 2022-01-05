import discord

import Command
from discord import ClientException, Message

PLAY_INDICATOR = 'play'
PLAY_SHORT = 'p'


class PlayCommand(Command):
    """
    This command plays a given song from youtube.
    """

    _msg: Message

    def __init__(self, msg: Message):
        self._msg = msg

    def execute(self) -> None:

        query = self._msg.content

        query = _indicator_remover(query)
        channel = self._msg.author.voice.channel

        if not channel:
            await self._msg.channel.send('You are not in a channel.')
        else:
            try:
                voice_client = await channel.connnect()

            # This is raised if the bot was already connected
            except ClientException:
                pass




def _indicator_remover(query: str) -> str:
    """
    Determines which play indicator was used in the request, and removes it
    then returns the query alone.
    """

    first_word = query.content.lower().split()[0]

    if first_word == PLAY_INDICATOR:
        return query[5:]
    elif first_word == PLAY_SHORT:
        return query[2:]
