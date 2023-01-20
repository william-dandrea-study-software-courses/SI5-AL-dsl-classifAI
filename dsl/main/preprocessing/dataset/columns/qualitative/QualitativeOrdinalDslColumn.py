from typing import List, cast

from dsl.main.preprocessing.cleaning_methods.DslCleaningMethod import DslCleaningMethod
from dsl.main.preprocessing.dataset.columns.qualitative.QualitativeDslColumn import QualitativeDslColumn
from utils.dataset.column.qualitative.OrdinalQualitativeColumn import OrdinalQualitativeColumn


class QualitativeOrdinalDslColumn(QualitativeDslColumn):

    def __init__(self, name: str, values: List[str], use_default_transformation: bool,
                 cleaning_method: DslCleaningMethod):
        super().__init__(name, values, use_default_transformation, cleaning_method)
        self.__column: OrdinalQualitativeColumn = None

    def export(self) -> OrdinalQualitativeColumn:
        if self.__column is not None:
            return self.__column

        self.__column: OrdinalQualitativeColumn = OrdinalQualitativeColumn()
        self.__column.set_name(self._name)

        for val in self._values:
            self.__column.add_possible_value(val)

        self.__column.set_cleaning_method(self._cleaning_method.export())
        self.__column.set_default_transformation(self._use_default_transformation)

        return self.__column
