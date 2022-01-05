from typing import Optional
from Handler import BaseHandler
from discord import Message
from Code.Commands import Command, PlayCommand

PLAY_INDICATORS = ['play', 'p']


class MusicHandler(BaseHandler):
    """
    The Handler for music requests.
    """

    def Handle(self, request: Message) -> Optional[Command]:

        first_word = request.content.lower().split()[0]

        if first_word in PLAY_INDICATORS:
            return PlayCommand(request)
        else:
            return super().Handle(request)
