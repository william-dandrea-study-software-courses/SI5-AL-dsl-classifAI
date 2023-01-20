from typing import List

from domain.main.utils.dataset.column.Column import Column


class Dataset:

    def __init__(self):
        self.__columns: List[Column] = []

    def add_column(self, column: Column):
        self.__columns.append(column)

    def get_columns(self) -> List[Column]:
        return self.__columns
