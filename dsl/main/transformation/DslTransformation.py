from dsl.main.DslStep import DslStep
from dsl.main.preprocessing.dataset.DslDataset import DslDataset


class DslTransformation(DslStep):
    def __init__(self):
        super().__init__()
        self.__dataset: DslDataset = None

    def dataset(self, dataset: DslDataset):
        self.__dataset = dataset
