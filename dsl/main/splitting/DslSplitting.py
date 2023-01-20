from dsl.main.DslStep import DslStep
from dsl.main.preprocessing.dataset.DslDataset import DslDataset
from steps.splitting.Splitting import Splitting
from utils.dataset.Dataset import Dataset


class DslSplitting(DslStep):
    def __init__(self):
        super().__init__()
        self.__train_percent = 0.7
        self.__validation_percent = 0.15
        self.__test_percent = 0.15
        self.__dataset: DslDataset = None
        self.__splitting: Splitting = None

    def train_validation_test(self, train_percent: float = 0.7, validation_percent: float = 0.15,
                              test_percent: float = 0.15):
        self.__train_percent = train_percent
        self.__validation_percent = validation_percent
        self.__test_percent = test_percent

    def dataset(self, dataset: DslDataset):
        self.__dataset = dataset

    def export(self) -> Splitting:

        if self.__splitting is not None:
            return self.__splitting

        if self.__dataset is None:
            raise ValueError("Cannot export without dataset")

        self.__splitting: Splitting = Splitting(dataset=self.__dataset.export())
        self.__splitting.set_train_dataset_percentage(self.__train_percent)
        self.__splitting.set_validation_dataset_percentage(self.__validation_percent)
        self.__splitting.set_test_dataset_percentage(self.__test_percent)
        return self.__splitting
