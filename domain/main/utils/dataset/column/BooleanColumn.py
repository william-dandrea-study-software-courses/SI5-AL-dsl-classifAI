from typing import List

from domain.main.utils.dataset.column.Column import Column


class BooleanColumn(Column):
    def __init__(self):
        super().__init__()
        self.__true_value: str = ""
        self.__false_value: str = ""
        self.__is_label: bool = False

    def set_true_value(self, value: str):
        self.__true_value = value

    def set_false_value(self, value: str):
        self.__false_value = value

    def set_is_label(self):
        self.__is_label = True

    def get_is_label(self) -> bool:
        return self.__is_label

    def is_label(self) -> bool:
        return self.__is_label

    def get_true_value(self) -> str:
        return self.__true_value

    def get_false_value(self) -> str:
        return self.__false_value

    def get_possible_values(self) -> List[str]:
        return [
            f"True value = {self.__true_value}",
            f"False value = {self.__false_value}"
        ]

    def get_type(self) -> str:
        return "Boolean"


    def export_transformation(self):

        code_cell = ""

        if not self.__is_label and self.get_default_transformation():
            replacement = {self.__true_value: True, self.__false_value: False}
            code_cell += f'\tX_train["{self.get_name()}"] = X_train["{self.get_name()}"].map({replacement})\n' \
                         f'\tX_val["{self.get_name()}"] = X_val["{self.get_name()}"].map({replacement})\n' \
                         f'\tX_test["{self.get_name()}"] = X_test["{self.get_name()}"].map({replacement})\n' \
                         f'\t\n'

        return code_cell
