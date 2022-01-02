from typing import Optional

from Code.Commands import *


class Handler(ABC):
    """
    A class that defines the interface for all handler subclasses. They will
    determine which command is correct for handling the current given request.
    """

    @abstractmethod
    def Handle(self, request: Message) -> Optional[Command]:
        pass


class BaseHandler(Handler):
    """
    The basic Handler from which all others inherit.
    """

    _next: Handler

    def set_next(self, next_handler: Handler):
        self._next = next_handler

    def Handle(self, request) -> Optional[Command]:
        if self._next:
            return self._next.Handle(request)

        return None


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