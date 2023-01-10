from domain.main.steps.Step import Step


class Splitting(Step):

    def __init__(self):
        super().__init__()
        self.train_dataset_percentage: float = 0.7
        self.validation_dataset_percentage: float = 0.15
        self.test_dataset_percentage: float = 0.15

    def set_train_dataset_percentage(self, percentage: float):
        self.train_dataset_percentage = percentage

    def set_validation_dataset_percentage(self, percentage: float):
        self.validation_dataset_percentage = percentage

    def set_test_dataset_percentage(self, percentage: float):
        self.test_dataset_percentage = percentage
