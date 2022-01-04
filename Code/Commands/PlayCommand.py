import Command
from discord import Message

PLAY_INDICATORS = ['play', 'p']


class PlayCommand(Command):
    """
    This command plays a given song from youtube.
    """

    _msg: Message

    def __init__(self, msg: Message):
        self._msg = msg

    def execute(self) -> None:
        pass  # TODO
