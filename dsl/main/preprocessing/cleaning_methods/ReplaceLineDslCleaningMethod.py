from dsl.main.preprocessing.cleaning_methods.DslCleaningMethod import DslCleaningMethod
from steps.preprocessing.cleaning.ReplaceLineCleaningMethod import ReplaceLineCleaningMethod


class ReplaceLineDslCleaningMethod(DslCleaningMethod):
    def __init__(self, replace_by):
        super().__init__()
        self.__replace_by = replace_by

    def export(self) -> ReplaceLineCleaningMethod:
        return ReplaceLineCleaningMethod(replace_by=self.__replace_by)
