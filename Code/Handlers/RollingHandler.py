from typing import Optional
from Handler import BaseHandler
from discord import Message
from Code.Commands import Command, RollCommand


class RollingHandler(BaseHandler):
    """
    The handler for rolling requests.
    """

    def Handle(self, request: Message) -> Optional[Command]:

        first_word = request.content.lower().split()[0]

        if first_word == "roll":
            return RollCommand(request)
        else:
            return super().Handle(request)
