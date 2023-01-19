from abc import abstractmethod, ABC

from steps.preprocessing.cleaning.CleaningMethod import CleaningMethod


class DslCleaningMethod(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def export(self) -> CleaningMethod:
        pass
