from abc import ABC, abstractmethod

from dsl.main.preprocessing.cleaning_methods.DeleteLineDslCleaningMethod import DeleteLineDslCleaningMethod
from dsl.main.preprocessing.cleaning_methods.DslCleaningMethod import DslCleaningMethod
from utils.dataset.column.Column import Column


class DslColumn(ABC):

    def __init__(self, name: str, use_default_transformation: bool, cleaning_method: DslCleaningMethod):
        self._name: str = name
        self._use_default_transformation: bool = use_default_transformation
        self._cleaning_method: DslCleaningMethod = cleaning_method

    def get_name(self) -> str:
        return self._name

    def get_use_default_transformation(self) -> bool:
        return self._use_default_transformation

    def get_cleaning_method(self) -> DslCleaningMethod:
        return self._cleaning_method

    @abstractmethod
    def export(self) -> Column:
        pass
