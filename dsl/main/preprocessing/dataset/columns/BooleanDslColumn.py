from dsl.main.preprocessing.cleaning_methods.DeleteLineDslCleaningMethod import DeleteLineDslCleaningMethod
from dsl.main.preprocessing.cleaning_methods.DslCleaningMethod import DslCleaningMethod
from dsl.main.preprocessing.cleaning_methods.ReplaceLineDslCleaningMethod import ReplaceLineDslCleaningMethod
from dsl.main.preprocessing.dataset.columns.DslColumn import DslColumn
from steps.preprocessing.cleaning.DeleteLineCleaningMethod import DeleteLineCleaningMethod
from steps.preprocessing.cleaning.ReplaceLineCleaningMethod import ReplaceLineCleaningMethod
from utils.dataset.column.BooleanColumn import BooleanColumn


class BooleanDslColumn(DslColumn):

    def __init__(self, name: str, true_value: str, false_value: str, cleaning_method: DslCleaningMethod,
                 use_default_transformation: bool, is_label: bool = False):
        super().__init__(name, use_default_transformation, cleaning_method)
        self.__true_value: str = true_value
        self.__false_value: str = false_value
        self.__is_label: bool = is_label

    def export(self) -> BooleanColumn:
        column: BooleanColumn = BooleanColumn()
        column.set_true_value(self.__true_value)
        column.set_false_value(self.__false_value)
        column.set_name(self._name)
        column.set_default_transformation(self._use_default_transformation)

        if self.__is_label:
            column.set_is_label()

        column.set_cleaning_method(self._cleaning_method.export())

        return column
