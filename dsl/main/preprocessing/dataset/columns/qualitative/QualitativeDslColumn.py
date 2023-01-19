from typing import List, cast

from dsl.main.preprocessing.cleaning_methods.DeleteLineDslCleaningMethod import DeleteLineDslCleaningMethod
from dsl.main.preprocessing.cleaning_methods.DslCleaningMethod import DslCleaningMethod
from dsl.main.preprocessing.cleaning_methods.ReplaceLineDslCleaningMethod import ReplaceLineDslCleaningMethod
from dsl.main.preprocessing.dataset.columns.DslColumn import DslColumn
from steps.preprocessing.cleaning.DeleteLineCleaningMethod import DeleteLineCleaningMethod
from steps.preprocessing.cleaning.ReplaceLineCleaningMethod import ReplaceLineCleaningMethod
from utils.dataset.column.Column import Column
from utils.dataset.column.qualitative.QualitativeColumn import QualitativeColumn


class QualitativeDslColumn(DslColumn):

    def __init__(self, name: str, values: List[str], use_default_transformation: bool,
                 cleaning_method: DslCleaningMethod):
        super().__init__(name, use_default_transformation, cleaning_method)
        self._values = values

    def export(self) -> QualitativeColumn:
        self._export_qualitative_column()

    def _export_qualitative_column(self) -> QualitativeColumn:
        column: QualitativeColumn = QualitativeColumn()
        column.set_name(self._name)
        column.set_default_transformation(self._use_default_transformation)
        column.set_cleaning_method(self._cleaning_method.export())

        for val in self._values:
            column.add_possible_value(val)

        return column
