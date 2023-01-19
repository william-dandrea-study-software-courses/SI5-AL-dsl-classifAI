from typing import List, cast

from dsl.main.preprocessing.cleaning_methods.DslCleaningMethod import DslCleaningMethod
from dsl.main.preprocessing.dataset.columns.qualitative.QualitativeDslColumn import QualitativeDslColumn
from utils.dataset.column.qualitative.OrdinalQualitativeColumn import OrdinalQualitativeColumn


class QualitativeOrdinalDslColumn(QualitativeDslColumn):

    def __init__(self, name: str, values: List[str], use_default_transformation: bool,
                 cleaning_method: DslCleaningMethod):
        super().__init__(name, values, use_default_transformation, cleaning_method)

    def export(self) -> OrdinalQualitativeColumn:
        return cast(OrdinalQualitativeColumn, self._export_qualitative_column())
