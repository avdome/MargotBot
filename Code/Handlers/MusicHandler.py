from typing import Optional
from Handler import BaseHandler
from discord import Message
from Code.Commands import Command, PlayCommand


class MusicHandler(BaseHandler):
    """
    The Handler for music requests.
    """

    def Handle(self, request: Message) -> Optional[Command]:

        first_word = request.content.lower().split()[0]

        if first_word == 'play':
            return PlayCommand(request)
        else:
            return super().Handle(request)
