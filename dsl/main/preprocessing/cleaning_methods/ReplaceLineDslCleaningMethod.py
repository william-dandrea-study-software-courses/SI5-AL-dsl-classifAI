from dsl.main.preprocessing.cleaning_methods.DslCleaningMethod import DslCleaningMethod


class ReplaceLineDslCleaningMethod(DslCleaningMethod):
    def __init__(self, replace_by):
        super().__init__()
        self.__replace_by = replace_by
