from abc import ABC, abstractmethod

from dsl.main.preprocessing.cleaning_methods.DeleteLineDslCleaningMethod import DeleteLineDslCleaningMethod
from dsl.main.preprocessing.cleaning_methods.DslCleaningMethod import DslCleaningMethod
from utils.dataset.column.Column import Column


class DslColumn(ABC):

    def __init__(self, name: str, use_default_transformation: bool, cleaning_method: DslCleaningMethod):
        self._name = name
        self._use_default_transformation = use_default_transformation
        self._cleaning_method: DslCleaningMethod = cleaning_method

    @abstractmethod
    def export(self) -> Column:
        pass
