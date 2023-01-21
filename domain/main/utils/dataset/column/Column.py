from abc import ABC, abstractmethod
from enum import Enum
from typing import List

from steps.preprocessing.cleaning.CleaningMethod import CleaningMethod
from steps.preprocessing.cleaning.DeleteLineCleaningMethod import DeleteLineCleaningMethod


class Column(ABC):

    def __init__(self):
        self.__default_transformation: bool = True
        self.__name: str = ""
        self.__cleaning_method: CleaningMethod = DeleteLineCleaningMethod()

    def set_default_transformation(self, is_default: bool) -> None:
        self.__default_transformation = is_default

    def set_name(self, name: str) -> None:
        self.__name = name

    def set_cleaning_method(self, cleaning_method: CleaningMethod) -> None:
        self.__cleaning_method = cleaning_method

    def get_name(self) -> str:
        return self.__name

    @abstractmethod
    def get_type(self) -> str:
        return "Column"

    @abstractmethod
    def is_label(self) -> bool:
        return False

    @abstractmethod
    def get_possible_values(self) -> List[str]:
        return []

    def get_default_transformation(self) -> bool:
        return self.__default_transformation

    def get_cleaning_method(self) -> CleaningMethod:
        return self.__cleaning_method


    @abstractmethod
    def export_transformation(self) -> str:
        pass
