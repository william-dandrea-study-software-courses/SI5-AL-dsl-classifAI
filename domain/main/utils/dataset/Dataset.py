from typing import List

from domain.main.utils.dataset.column.Column import Column


class Dataset:

    def __init__(self):
        self.__columns: List[Column] = []
        self.__use_default_transformation: bool = True

    def add_column(self, column: Column):
        self.__columns.append(column)

    def change_use_default_transformation(self, use_default: bool):
        self.__use_default_transformation = use_default

    def get_columns(self) -> List[Column]:
        return self.__columns

