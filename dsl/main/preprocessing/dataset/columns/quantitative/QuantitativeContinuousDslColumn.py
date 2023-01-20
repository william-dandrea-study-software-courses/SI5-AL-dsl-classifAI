from typing import cast

from dsl.main.preprocessing.cleaning_methods.DslCleaningMethod import DslCleaningMethod
from dsl.main.preprocessing.dataset.columns.quantitative.QuantitativeDslColumn import QuantitativeDslColumn
from utils.dataset.column.quantitative.ContinuousQuantitativeColumn import ContinuousQuantitativeColumn


class QuantitativeContinuousDslColumn(QuantitativeDslColumn):
    def __init__(self, name: str, use_default_transformation: bool, cleaning_method: DslCleaningMethod):
        super().__init__(name, use_default_transformation, cleaning_method)
        self.__column: ContinuousQuantitativeColumn = None

    def export(self) -> ContinuousQuantitativeColumn:
        if self.__column is not None:
            return self.__column

        self.__column: ContinuousQuantitativeColumn = ContinuousQuantitativeColumn()
        self.__column.set_name(self._name)
        self.__column.set_default_transformation(self._use_default_transformation)
        self.__column.set_cleaning_method(self._cleaning_method.export())

        return self.__column
