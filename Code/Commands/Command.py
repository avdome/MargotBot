from abc import ABC, abstractmethod


class Command(ABC):
    """
    This is an abstract class that defines the interface for all commands
    that our bot can execute.
    """

    @abstractmethod
    def execute(self) -> None:
        pass



