from dsl.main.DslStep import DslStep
from dsl.main.preprocessing.dataset.DslDataset import DslDataset


class DslPreprocessing(DslStep):

    def __init__(self):
        super().__init__()
        self.dataset: DslDataset = None

    def dataset_file(self, path: str):
        self.dataset = DslDataset(path=path)
