from typing import List, Tuple

import nbformat
import networkx as nx
import numpy as np

from graphviz import Digraph
from matplotlib import pyplot as plt

from domain.main.steps.Step import Step
from steps.preprocessing.cleaning.DeleteLineCleaningMethod import DeleteLineCleaningMethod
from steps.preprocessing.cleaning.ReplaceLineCleaningMethod import ReplaceLineCleaningMethod
from utils.Cell import Cell, CellTypeEnum
from utils.Import import Import
from utils.dataset.Dataset import Dataset
from utils.utils import generate_markdown_array


class Preprocessing(Step):

    def __init__(self, url_dataset: str, is_dataset_contains_headers_name: bool = False):
        super().__init__()
        self.__url_dataset = url_dataset
        self.__is_dataset_contains_headers_name = is_dataset_contains_headers_name
        self.__dataset: Dataset = None

    def get_url_dataset(self) -> str:
        return self.__url_dataset

    def add_dataset(self, dataset: Dataset):
        self.__dataset = dataset

    def export(self) -> List[Cell]:
        if self.__dataset is None:
            raise Exception("A dataset is required for generate the Jupyter notebook file")

        column_names: List[str] = [col.get_name() for col in self.__dataset.get_columns()]
        if len(column_names) != len(set(column_names)):
            raise ValueError("A dataset cannot have 2 columns with the same name")

        self._imports.append(Import(package="pandas", method=None, as_name="pd"))
        self._imports.append(Import(package="numpy", method=None, as_name="np"))

        cells: List[Cell] = [Cell("import warnings\nwarnings.filterwarnings('ignore')", CellTypeEnum.CODE)]

        cells.append(Cell(f'![alt text]({f"{self.__url_dataset}_mindmap.png"} "Mindmap")', CellTypeEnum.MARKDOWN))

        description_content = f"# Préprocessing" + '\n'
        description_content += self.__generate_table_with_columns_details()
        cells.append(Cell(description_content, CellTypeEnum.MARKDOWN))

        load_description_content = f"## We import the dataset"
        cells.append(Cell(load_description_content, CellTypeEnum.MARKDOWN))

        cell_code_load = f'def load_dataset() -> pd.DataFrame: \n' \
                         f'\tcurrent_dataset = pd.read_csv("{self.__url_dataset}", header={1 if self.__is_dataset_contains_headers_name else None}) \n' \
                         f'\tcurrent_dataset.columns = {[col.get_name() for col in self.__dataset.get_columns()]} \n' \
                         f'\treturn current_dataset \n' \
                         f'\n' \
                         f'dataframe: pd.DataFrame = load_dataset() \n' \
                         f'dataframe'
        cells.append(Cell(cell_code_load, CellTypeEnum.CODE))

        cell_code_cleaning = f'def clean_dataset(dataframe: pd.DataFrame) -> pd.DataFrame:\n' \
                             f'\tdataframe = dataframe.replace("?", np.nan)\n'

        for col in self.__dataset.get_columns():

            if col.get_cleaning_method().__class__.__name__ == DeleteLineCleaningMethod.__name__:
                cell_code_cleaning += f'\tdataframe = dataframe[dataframe["{col.get_name()}"].notna()]\n'

            if col.get_cleaning_method().__class__.__name__ == ReplaceLineCleaningMethod.__name__:
                cleaning_method: ReplaceLineCleaningMethod = col.get_cleaning_method()
                cell_code_cleaning += f'\tdataframe["{col.get_name()}"] = dataframe["{col.get_name()}"].replace(np.nan, {cleaning_method.get_replace_by()})\n'

        cell_code_cleaning += f'\treturn dataframe.reset_index(drop=True)\n'
        cell_code_cleaning += f'\ndataframe: pd.DataFrame = load_dataset()\n'
        cell_code_cleaning += f'\ncleaned_dataframe = clean_dataset(dataframe)\n'
        cell_code_cleaning += f'cleaned_dataframe\n'
        cells.append(Cell(cell_code_cleaning, CellTypeEnum.CODE))

        return cells

    def __generate_table_with_columns_details(self) -> str:
        return generate_markdown_array(
            column_names=["Column name", "Column type", "Use default transformation ?", "Cleaning method", "Possible values", "Is Label ?"],
            columns_values=[
                [
                    column.get_name(),
                    column.get_type(),
                    "Yes" if column.get_default_transformation() else "No",
                    column.get_cleaning_method().get_type(),
                    " / ".join(column.get_possible_values()),
                    "Yes" if column.is_label() else "No"
                ] for column in self.__dataset.get_columns()
            ]
        )
