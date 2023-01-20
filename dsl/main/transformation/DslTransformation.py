from dsl.main.DslStep import DslStep
from dsl.main.preprocessing.dataset.DslDataset import DslDataset
from steps.transformation.Transformation import Transformation


class DslTransformation(DslStep):
    def __init__(self):
        super().__init__()
        self.__dataset: DslDataset = None
        self.__transformation: Transformation = None

    def dataset(self, dataset: DslDataset):
        self.__dataset = dataset

    def export(self) -> Transformation:
        if self.__transformation is not None:
            return self.__transformation

        if self.__dataset is None:
            raise ValueError("Cannot export without dataset")

        self.__transformation = Transformation(self.__dataset.export())
        return self.__transformation
