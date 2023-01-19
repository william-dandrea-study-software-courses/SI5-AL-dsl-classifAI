from typing import cast

from dsl.main.preprocessing.cleaning_methods.DslCleaningMethod import DslCleaningMethod
from dsl.main.preprocessing.dataset.columns.quantitative.QuantitativeDslColumn import QuantitativeDslColumn
from utils.dataset.column.quantitative.ContinuousQuantitativeColumn import ContinuousQuantitativeColumn


class QuantitativeContinuousDslColumn(QuantitativeDslColumn):
    def __init__(self, name: str, use_default_transformation: bool, cleaning_method: DslCleaningMethod):
        super().__init__(name, use_default_transformation, cleaning_method)

    def export(self) -> ContinuousQuantitativeColumn:
        return cast(ContinuousQuantitativeColumn, self._export_quantitative_column())
