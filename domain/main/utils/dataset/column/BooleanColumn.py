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
