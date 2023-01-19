from typing import List

from dsl.main.preprocessing.dataset.columns.qualitative.QualitativeDslColumn import QualitativeDslColumn


class QualitativeOrdinalDslColumn(QualitativeDslColumn):

    def __init__(self, name: str, values: List[str], use_default_transformation: bool):
        super().__init__(name, values, use_default_transformation)
