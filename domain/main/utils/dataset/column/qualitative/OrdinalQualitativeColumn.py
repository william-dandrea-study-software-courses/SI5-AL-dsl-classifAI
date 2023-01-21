from domain.main.utils.dataset.column.Column import Column
from utils.dataset.column.qualitative.QualitativeColumn import QualitativeColumn


class OrdinalQualitativeColumn(QualitativeColumn):
    def __init__(self):
        super().__init__()

    def get_type(self) -> str:
        return "Ordinal Qualitative"

    def export_transformation(self):

        code_cell = ""

        if self.get_default_transformation():
            code_cell += f'\tordinal_encoder = OrdinalEncoder(categories=[{self.get_possible_values()}])\n' \
                         f'\tX_train["{self.get_name()}"] = ordinal_encoder.fit_transform(X_train[["{self.get_name()}"]])\n' \
                         f'\tX_val["{self.get_name()}"] = ordinal_encoder.fit_transform(X_val[["{self.get_name()}"]])\n' \
                         f'\tX_test["{self.get_name()}"] = ordinal_encoder.fit_transform(X_test[["{self.get_name()}"]])\n' \
                         f'\t\n'

        return code_cell
