from abc import ABC, abstractmethod
from discord import Message

from Code.Roller import *


class Command(ABC):
    """
    This is an abstract class that defines the interface for all commands
    that our bot can execute.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class LoveResponse(Command):
    """
    This is a command that responds with "I love you too <3" to the user.
    """

    _msg: Message

    def __init__(self, msg: Message):
        self._msg = msg

    def execute(self) -> None:
        await self._msg.channel.send('Margot loves you too <3')


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


class PlayCommand(Command):
    """
    This command plays a given song from youtube.
    """

    _msg: Message

    def __init__(self, msg: Message):
        self._msg = msg

    def execute(self) -> None:
        pass  # TODO
