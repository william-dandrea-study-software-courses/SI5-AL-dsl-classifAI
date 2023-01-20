from typing import cast

from dsl.main.preprocessing.cleaning_methods.DslCleaningMethod import DslCleaningMethod
from steps.preprocessing.cleaning.CleaningMethod import CleaningMethod
from steps.preprocessing.cleaning.ReplaceLineCleaningMethod import ReplaceLineCleaningMethod


class ReplaceLineDslCleaningMethod(DslCleaningMethod):

    def __init__(self, replace_by):
        super().__init__()
        self.__replace_by = replace_by

    def export(self) -> ReplaceLineCleaningMethod:
        if self._cleaning_method is not None:
            return cast(ReplaceLineCleaningMethod, self._cleaning_method)

        self._cleaning_method: ReplaceLineCleaningMethod = ReplaceLineCleaningMethod(replace_by=self.__replace_by)
        return self._cleaning_method
