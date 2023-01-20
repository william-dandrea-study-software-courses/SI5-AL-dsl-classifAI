from typing import cast

from dsl.main.preprocessing.cleaning_methods.DslCleaningMethod import DslCleaningMethod
from steps.preprocessing.cleaning.DeleteLineCleaningMethod import DeleteLineCleaningMethod


class DeleteLineDslCleaningMethod(DslCleaningMethod):

    def __init__(self):
        super().__init__()

    def export(self) -> DeleteLineCleaningMethod:
        if self._cleaning_method is not None:
            return cast(DeleteLineCleaningMethod, self._cleaning_method)

        self._cleaning_method: DeleteLineCleaningMethod = DeleteLineCleaningMethod()
        return self._cleaning_method
