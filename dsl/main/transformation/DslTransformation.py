from dsl.main.DslStep import DslStep
from dsl.main.preprocessing.dataset.DslDataset import DslDataset
from steps.transformation.Transformation import Transformation


class DslTransformation(DslStep):
    def __init__(self):
        super().__init__()
        self.__dataset: DslDataset = None

    def dataset(self, dataset: DslDataset):
        self.__dataset = dataset

    def export(self) -> Transformation:
        return None
