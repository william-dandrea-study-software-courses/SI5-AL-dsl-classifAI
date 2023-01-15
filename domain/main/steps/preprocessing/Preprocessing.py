from typing import List, Tuple

import nbformat

from domain.main.steps.Step import Step
from steps.preprocessing.cleaning.DeleteLineCleaningMethod import DeleteLineCleaningMethod
from steps.preprocessing.cleaning.ReplaceLineCleaningMethod import ReplaceLineCleaningMethod
from utils.Cell import Cell, CellTypeEnum
from utils.Import import Import
from utils.dataset.Dataset import Dataset


class Preprocessing(Step):

    def __init__(self, url_dataset: str, is_dataset_contains_headers_name: bool = False):
        super().__init__()
        self.__url_dataset = url_dataset
        self.__is_dataset_contains_headers_name = is_dataset_contains_headers_name
        self.__dataset: Dataset = None



    def add_dataset(self, dataset: Dataset):
        self.__dataset = dataset

    def export(self) -> List[Cell]:
        if self.__dataset is None:
            raise Exception("A dataset is required for generate the Jupyter notebook file")

        self._imports.append(Import(package="pandas", method=None, as_name="pd"))
        self._imports.append(Import(package="numpy", method=None, as_name="np"))

        cells: List[Cell] = []

        description_content = f"# Préprocessing"
        cells.append(Cell(description_content, CellTypeEnum.MARKDOWN))

        load_description_content = f"## We import the dataset"
        cells.append(Cell(load_description_content, CellTypeEnum.MARKDOWN))

        cell_code_load = f'def load_dataset(dataset_url: str) -> pd.DataFrame: \n' \
                    f'\tcurrent_dataset = pd.read_csv(dataset_url, header={1 if self.__is_dataset_contains_headers_name else None}) \n' \
                    f'\tcurrent_dataset.columns = {[col.get_name() for col in self.__dataset.get_columns()]} \n' \
                    f'\treturn current_dataset \n' \
                    f'\n' \
                    f'dataframe: pd.DataFrame = load_dataset("{self.__url_dataset}") \n' \
                    f'dataframe'
        cells.append(Cell(cell_code_load, CellTypeEnum.CODE))

        cell_code_cleaning = f'def clean_dataset(dataframe: pd.DataFrame) -> pd.DataFrame:\n' \
                             f'\tdataframe = dataframe.replace("?", np.nan)\n'

        for col in self.__dataset.get_columns():

            if col.get_cleaning_method().__class__.__name__ == DeleteLineCleaningMethod.__name__:
                cell_code_cleaning += f'\tdataframe = dataframe[dataframe["{col.get_name()}"].notna()]\n' \

            if col.get_cleaning_method().__class__.__name__ == ReplaceLineCleaningMethod.__name__:
                cleaning_method: ReplaceLineCleaningMethod = col.get_cleaning_method()
                cell_code_cleaning += f'\tdataframe["{col.get_name()}"] = dataframe["{col.get_name()}"].replace(np.nan, {cleaning_method.get_replace_by()})\n'

        cell_code_cleaning += f'\treturn dataframe.reset_index()\n'
        cell_code_cleaning += f'\ncleaned_dataframe = clean_dataset(dataframe)\n'
        cell_code_cleaning += f'cleaned_dataframe\n'
        cells.append(Cell(cell_code_cleaning, CellTypeEnum.CODE))

        return cells


