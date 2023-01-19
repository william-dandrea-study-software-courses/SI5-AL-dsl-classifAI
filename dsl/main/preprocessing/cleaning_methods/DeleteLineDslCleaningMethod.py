from dsl.main.preprocessing.cleaning_methods.DslCleaningMethod import DslCleaningMethod
from steps.preprocessing.cleaning.DeleteLineCleaningMethod import DeleteLineCleaningMethod


class DeleteLineDslCleaningMethod(DslCleaningMethod):

    def __init__(self):
        super().__init__()

    def export(self) -> DeleteLineCleaningMethod:
        return DeleteLineCleaningMethod()
