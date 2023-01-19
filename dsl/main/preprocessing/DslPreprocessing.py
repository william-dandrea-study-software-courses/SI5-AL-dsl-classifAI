from dsl.main.DslStep import DslStep
from dsl.main.preprocessing.dataset.DslDataset import DslDataset
from steps.preprocessing.Preprocessing import Preprocessing


class DslPreprocessing(DslStep):

    def __init__(self):
        super().__init__()
        self.dataset: DslDataset = None
        self.__dataset_path: str = ""
        self.__is_dataset_contains_header: bool = False

    def dataset_file(self, path: str, is_dataset_contains_header: bool = False):
        self.dataset = DslDataset()
        self.__dataset_path = path
        self.__is_dataset_contains_header = is_dataset_contains_header


    def export(self) -> Preprocessing:

        preprocessing: Preprocessing = Preprocessing(self.__dataset_path, self.__is_dataset_contains_header)
        preprocessing.add_dataset(dataset=self.dataset.export())

        return preprocessing
