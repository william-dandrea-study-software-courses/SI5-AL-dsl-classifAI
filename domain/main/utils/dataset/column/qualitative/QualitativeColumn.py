from typing import List

from domain.main.utils.dataset.column.Column import Column


class QualitativeColumn(Column):
    def __init__(self):
        super().__init__()
        self.__possible_values: List[str] = []

    def add_possible_value(self, value: str):
        self.__possible_values.append(value)
