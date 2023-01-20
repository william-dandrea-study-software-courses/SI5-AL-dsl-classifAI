from typing import List

from domain.main.utils.dataset.column.Column import Column


class QuantitativeColumn(Column):
    def __init__(self):
        super().__init__()

    def get_type(self) -> str:
        return "Quantitative"

    def is_label(self) -> bool:
        return False

    def get_possible_values(self) -> List[str]:
        return []

