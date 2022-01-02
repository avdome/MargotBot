from abc import ABC, abstractmethod


class Handler(ABC):
    """
    A class that defines the interface for all handler subclasses. They will
    determine which command is correct for handling the current given request.
    """

    @abstractmethod
    def handle(self, request: str):
        pass

