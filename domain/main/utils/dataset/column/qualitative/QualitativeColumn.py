from typing import List

from domain.main.utils.dataset.column.Column import Column


class QualitativeColumn(Column):
    def __init__(self):
        super().__init__()
        self.__possible_values: List[str] = []

    def add_possible_value(self, value: str):
        self.__possible_values.append(value)

    def get_possible_values(self) -> List[str]:
        return self.__possible_values

    def get_type(self) -> str:
        return "Qualitative"

    def is_label(self) -> bool:
        return False

    def get_possible_values(self) -> List[str]:
        return self.__possible_values

