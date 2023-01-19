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

    def export(self) -> NominalQualitativeColumn:
        return cast(NominalQualitativeColumn, self._export_qualitative_column())
