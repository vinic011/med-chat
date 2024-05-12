from abc import ABC, abstractmethod

class Model(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def ask(self, question: str) -> str:
        pass