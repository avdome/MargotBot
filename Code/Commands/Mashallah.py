from discord import Message

import Command


class Mashallah(Command):
    """
       The command that responds to mashallah.
       """

    _msg: Message

    def __init__(self, msg: Message):
        self._msg = msg

    def execute(self) -> None:
        await self._msg.channel.send('لا إله إلا الله محمد رسول الله')

