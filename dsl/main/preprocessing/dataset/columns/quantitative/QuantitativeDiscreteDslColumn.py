from typing import cast

from dsl.main.preprocessing.cleaning_methods.DeleteLineDslCleaningMethod import DeleteLineDslCleaningMethod
from dsl.main.preprocessing.cleaning_methods.DslCleaningMethod import DslCleaningMethod
from dsl.main.preprocessing.cleaning_methods.ReplaceLineDslCleaningMethod import ReplaceLineDslCleaningMethod
from dsl.main.preprocessing.dataset.columns.quantitative.QuantitativeDslColumn import QuantitativeDslColumn
from steps.preprocessing.cleaning.DeleteLineCleaningMethod import DeleteLineCleaningMethod
from steps.preprocessing.cleaning.ReplaceLineCleaningMethod import ReplaceLineCleaningMethod
from utils.dataset.column.Column import Column
from utils.dataset.column.quantitative.DiscreteQuantitativeColumn import DiscreteQuantitativeColumn


class QuantitativeDiscreteDslColumn(QuantitativeDslColumn):

    def __init__(self, name: str, use_default_transformation: bool, cleaning_method: DslCleaningMethod):
        super().__init__(name, use_default_transformation, cleaning_method)

    def export(self) -> DiscreteQuantitativeColumn:
        return cast(DiscreteQuantitativeColumn, self._export_quantitative_column())
