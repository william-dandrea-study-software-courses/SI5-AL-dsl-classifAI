from typing import List

from domain.main.utils.dataset.column.Column import Column


class QuantitativeColumn(Column):
    def __init__(self):
        super().__init__()

    def get_type(self) -> str:
        return "Quantitative"

    def is_label(self) -> bool:
        return False

    def get_possible_values(self) -> List[str]:
        return []

    def export_transformation(self):

        code_cell = ""

        if self.get_default_transformation():
            code_cell += f'\tX_train["{self.get_name()}"] = X_train["{self.get_name()}"].astype(float) \n' \
                         f'\tX_val["{self.get_name()}"] = X_val["{self.get_name()}"].astype(float) \n' \
                         f'\tX_test["{self.get_name()}"] = X_test["{self.get_name()}"].astype(float) \n' \
                         f'\tX_train[["{self.get_name()}"]] = minmax_scale(X_train[["{self.get_name()}"]]) \n' \
                         f'\tX_val[["{self.get_name()}"]] = minmax_scale(X_val[["{self.get_name()}"]])\n' \
                         f'\tX_test[["{self.get_name()}"]] = minmax_scale(X_test[["{self.get_name()}"]])\n' \
                         f'\t\n'

        return code_cell
