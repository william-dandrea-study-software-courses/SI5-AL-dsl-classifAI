from dsl.main.preprocessing.cleaning_methods.DeleteLineDslCleaningMethod import DeleteLineDslCleaningMethod
from dsl.main.preprocessing.cleaning_methods.DslCleaningMethod import DslCleaningMethod
from dsl.main.preprocessing.dataset.columns.DslColumn import DslColumn


class BooleanDslColumn(DslColumn):

    def __init__(self, name: str, true_value: str, false_value: str, cleaning_method: DslCleaningMethod,
                 use_default_transformation: bool, is_label: bool):
        super().__init__(name, use_default_transformation)
        self.__true_value: str = true_value
        self.__false_value: str = false_value
        self.__cleaning_method: DslCleaningMethod = cleaning_method
        self.__is_label = is_label

