from domain.main.utils.dataset.column.Column import Column
from utils.dataset.column.quantitative.QuantitativeColumn import QuantitativeColumn


class DiscreteQuantitativeColumn(QuantitativeColumn):
    def __init__(self):
        super().__init__()

    def get_type(self) -> str:
        return "Quantitative Discrete"
