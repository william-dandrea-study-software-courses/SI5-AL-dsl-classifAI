from domain.main.utils.dataset.column.Column import Column


class BooleanColumn(Column):
    def __init__(self):
        super().__init__()
        self.true_value: str = ""
        self.false_value: str = ""
        self.is_label: bool = False

    def set_true_value(self, value: str):
        self.true_value = value

    def set_false_value(self, value: str):
        self.false_value = value

    def set_is_label(self):
        self.is_label = True
