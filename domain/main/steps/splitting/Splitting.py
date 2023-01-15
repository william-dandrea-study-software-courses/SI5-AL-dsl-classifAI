from domain.main.steps.Step import Step


class Splitting(Step):

    def __init__(self):
        super().__init__()
        self.__train_dataset_percentage: float = 0.7
        self.__validation_dataset_percentage: float = 0.15
        self.__test_dataset_percentage: float = 0.15

    def set_train_dataset_percentage(self, percentage: float):
        self.__train_dataset_percentage = percentage

    def set_validation_dataset_percentage(self, percentage: float):
        self.__validation_dataset_percentage = percentage

    def set_test_dataset_percentage(self, percentage: float):
        self.__test_dataset_percentage = percentage
