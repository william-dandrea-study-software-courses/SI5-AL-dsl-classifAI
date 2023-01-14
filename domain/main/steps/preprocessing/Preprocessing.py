from typing import List, Tuple

import nbformat

from domain.main.steps.Step import Step
from utils.Cell import Cell, CellTypeEnum
from utils.Import import Import
from utils.dataset.Dataset import Dataset


class Preprocessing(Step):

    def __init__(self, url_dataset: str, is_dataset_contains_headers_name: bool = False):
        super().__init__()
        self.url_dataset = url_dataset
        self.is_dataset_contains_headers_name = is_dataset_contains_headers_name
        self.dataset: Dataset = None

        self.imports: List[Import] = []

    def add_dataset(self, dataset: Dataset):
        self.dataset = dataset

    def generate(self) -> List[Cell]:
        if self.dataset is None:
            raise Exception("A dataset is required for generate the Jupyter notebook file")

        self.imports.append(Import(package="pandas", method=None, as_name="pd"))

        cells: List[Cell] = []

        description_content = f"# Préprocessing"
        cells.append(Cell(description_content, CellTypeEnum.MARKDOWN))

        load_description_content = f"## We import the dataset"
        cells.append(Cell(load_description_content, CellTypeEnum.MARKDOWN))

        cell_code = f'def load_dataset(dataset_url: str) -> pd.DataFrame: \n' \
                    f'\tcurrent_dataset = pd.read_csv(dataset_url, header={1 if self.is_dataset_contains_headers_name else None}) \n' \
                    f'\tcurrent_dataset.columns = {[col.name for col in self.dataset.columns]} \n' \
                    f'\treturn current_dataset \n' \
                    f'\n' \
                    f'load_dataset("{self.url_dataset}") \n' \
                    f''
        cells.append(Cell(cell_code, CellTypeEnum.CODE))

        return cells

    def get_imports(self) -> List[Import]:
        return self.imports
