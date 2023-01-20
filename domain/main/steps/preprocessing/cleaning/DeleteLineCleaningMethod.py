from steps.preprocessing.cleaning.CleaningMethod import CleaningMethod


class DeleteLineCleaningMethod(CleaningMethod):
    def __init__(self):
        super().__init__()

    def get_type(self):
        return "Delete Line"
