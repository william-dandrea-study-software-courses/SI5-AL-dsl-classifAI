from typing import List

from domain.main.steps.Step import Step
from utils.Cell import Cell, CellTypeEnum
from utils.Import import Import
from utils.dataset.Dataset import Dataset
from utils.dataset.column.BooleanColumn import BooleanColumn
from utils.dataset.column.qualitative.NominalQualitativeColumn import NominalQualitativeColumn
from utils.dataset.column.qualitative.OrdinalQualitativeColumn import OrdinalQualitativeColumn
from utils.dataset.column.quantitative.ContinuousQuantitativeColumn import ContinuousQuantitativeColumn
from utils.dataset.column.quantitative.DiscreteQuantitativeColumn import DiscreteQuantitativeColumn


class Transformation(Step):

    def __init__(self, dataset: Dataset):
        super().__init__()
        self.__dataset: Dataset = dataset

        self._imports.append(Import("sklearn.preprocessing", "minmax_scale"))
        self._imports.append(Import("sklearn.preprocessing", "OrdinalEncoder"))
        self._imports.append(Import("sklearn.preprocessing", "OneHotEncoder"))

    def export(self) -> List[Cell]:
        cells: List[Cell] = [Cell("# Transformation", CellTypeEnum.MARKDOWN)]

        code_cell: str = 'def transform_data(X_train, X_val, X_test):\n'
        for column in self.__dataset.get_columns():
            code_cell += column.export_transformation()

        code_cell += f'\treturn X_train, X_val, X_test\n'

        code_cell += f'\ndataframe: pd.DataFrame = load_dataset()\n'
        code_cell += f'cleaned_dataframe = clean_dataset(dataframe)\n'
        code_cell += f'X_train, y_train, X_val, y_val, X_test, y_test = split_data(cleaned_dataframe)\n'
        code_cell += f'X_train, X_val, X_test = transform_data(X_train, X_val, X_test)\n'
        code_cell += f'X_train\n'

        cells.append(Cell(code_cell, CellTypeEnum.CODE))

        return cells
