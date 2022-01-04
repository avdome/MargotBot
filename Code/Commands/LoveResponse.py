import Command
from discord import Message


class LoveResponse(Command):
    """
    This is a command that responds with "I love you too <3" to the user.
    """

    _msg: Message

    def __init__(self, msg: Message):
        self._msg = msg

    def execute(self) -> None:
        await self._msg.channel.send('Margot loves you too <3')
