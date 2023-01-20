from abc import abstractmethod, ABC


class CleaningMethod(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_type(self):
        return ""
