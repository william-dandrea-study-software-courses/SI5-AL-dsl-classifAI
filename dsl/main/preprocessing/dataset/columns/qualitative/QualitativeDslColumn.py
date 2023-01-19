from typing import List

from dsl.main.preprocessing.dataset.columns.DslColumn import DslColumn


class QualitativeDslColumn(DslColumn):

    def __init__(self, name: str, values: List[str], use_default_transformation: bool):
        super().__init__(name, use_default_transformation)
        self._values = values
