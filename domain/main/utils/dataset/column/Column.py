from abc import ABC, abstractmethod
from enum import Enum

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

    def get_cleaning_method(self):
        return self.__cleaning_method
