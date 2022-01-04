from typing import Optional
from Handler import BaseHandler
from discord import Message
from Code.Commands import Command, LoveResponse, Mashallah


class GeneralHandler(BaseHandler):
    """
    The handler for leftover miscellaneous requests.
    """

    def Handle(self, request: Message) -> Optional[Command]:

        content = request.content.lower()

        if content == 'margot':
            return LoveResponse()
        elif content == 'mashallah':
            return Mashallah()
        else:
            return super().Handle(request)
