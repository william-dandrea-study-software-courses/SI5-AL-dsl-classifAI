from steps.preprocessing.cleaning.CleaningMethod import CleaningMethod


class ReplaceLineCleaningMethod(CleaningMethod):
    def __init__(self, replace_by):
        super().__init__()
        self.__replace_by = replace_by

    def get_replace_by(self):
        return self.__replace_by
