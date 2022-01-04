import Command
from discord import Message
from Code.Roller import roll, rollcheck


class RollCommand(Command):
    """
    We do a little rolling.
    """

    _msg: Message

    def __init__(self, msg: Message):

        self._msg = msg

    def execute(self) -> None:

        rollnumber = rollcheck(self._msg.content.lower())
        if rollnumber > 0:
            await self._msg.channel.send(roll(rollnumber))

