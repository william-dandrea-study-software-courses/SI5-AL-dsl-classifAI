from dsl.main.DslStep import DslStep


class DslSplitting(DslStep):
    def __init__(self):
        super().__init__()
        self.__train_percent = 0.7
        self.__validation_percent = 0.15
        self.__test_percent = 0.15

    def train_validation_test(self, train_percent: float = 0.7, validation_percent: float = 0.15,
                              test_percent: float = 0.15):
        self.__train_percent = train_percent
        self.__validation_percent = validation_percent
        self.__test_percent = test_percent
