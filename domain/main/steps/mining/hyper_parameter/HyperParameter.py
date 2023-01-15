from abc import ABC, abstractmethod


class HyperParameter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_sklearn_name(self) -> str:
        pass
