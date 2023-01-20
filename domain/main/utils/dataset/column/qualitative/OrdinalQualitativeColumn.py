from domain.main.utils.dataset.column.Column import Column
from utils.dataset.column.qualitative.QualitativeColumn import QualitativeColumn


class OrdinalQualitativeColumn(QualitativeColumn):
    def __init__(self):
        super().__init__()

    def get_type(self) -> str:
        return "Ordinal Qualitative"

