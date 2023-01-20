from typing import List, cast

from dsl.main.preprocessing.cleaning_methods.DeleteLineDslCleaningMethod import DeleteLineDslCleaningMethod
from dsl.main.preprocessing.cleaning_methods.DslCleaningMethod import DslCleaningMethod
from dsl.main.preprocessing.cleaning_methods.ReplaceLineDslCleaningMethod import ReplaceLineDslCleaningMethod
from dsl.main.preprocessing.dataset.columns.qualitative.QualitativeDslColumn import QualitativeDslColumn
from steps.preprocessing.cleaning.DeleteLineCleaningMethod import DeleteLineCleaningMethod
from steps.preprocessing.cleaning.ReplaceLineCleaningMethod import ReplaceLineCleaningMethod
from utils.dataset.column.Column import Column
from utils.dataset.column.qualitative.NominalQualitativeColumn import NominalQualitativeColumn


class QualitativeNominalDslColumn(QualitativeDslColumn):

    def __init__(self, name: str, values: List[str], use_default_transformation: bool,
                 cleaning_method: DslCleaningMethod):
        super().__init__(name, values, use_default_transformation, cleaning_method)
        self.__column: NominalQualitativeColumn = None

    def export(self) -> NominalQualitativeColumn:
        if self.__column is not None:
            return self.__column

        self.__column: NominalQualitativeColumn = NominalQualitativeColumn()
        self.__column.set_name(self._name)

        for val in self._values:
            self.__column.add_possible_value(val)

        self.__column.set_cleaning_method(self._cleaning_method.export())
        self.__column.set_default_transformation(self._use_default_transformation)

        return self.__column
