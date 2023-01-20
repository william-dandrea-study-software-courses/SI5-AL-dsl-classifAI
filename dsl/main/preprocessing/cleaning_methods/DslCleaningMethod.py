from abc import abstractmethod, ABC

from steps.preprocessing.cleaning.CleaningMethod import CleaningMethod


class DslCleaningMethod(ABC):

    def __init__(self):
        self._cleaning_method: CleaningMethod = None

    @abstractmethod
    def export(self) -> CleaningMethod:
        pass
