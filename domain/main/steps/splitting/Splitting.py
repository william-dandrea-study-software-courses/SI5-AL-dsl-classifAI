from typing import List

from domain.main.steps.Step import Step
from utils.Cell import Cell, CellTypeEnum
from utils.Import import Import
from utils.dataset.Dataset import Dataset
from utils.dataset.column.BooleanColumn import BooleanColumn


class Splitting(Step):

    def __init__(self, dataset: Dataset):
        super().__init__()
        self.__train_dataset_percentage: float = 0.7
        self.__validation_dataset_percentage: float = 0.15
        self.__test_dataset_percentage: float = 0.15
        self.__dataset = dataset

        self._imports.append(Import("sklearn.model_selection", "train_test_split"))

    def set_train_dataset_percentage(self, percentage: float):
        self.__train_dataset_percentage = percentage

    def set_validation_dataset_percentage(self, percentage: float):
        self.__validation_dataset_percentage = percentage

    def set_test_dataset_percentage(self, percentage: float):
        self.__test_dataset_percentage = percentage

    def export(self) -> List[Cell]:

        cells: List[Cell] = [Cell("# Splitting", CellTypeEnum.MARKDOWN)]

        label_column_name = None
        for col in self.__dataset.get_columns():
            if col.__class__.__name__ == BooleanColumn.__name__:
                label_column_name = col.get_name()

        if label_column_name is None:
            raise ValueError("Cannot find the label column")

        code: str = f'def split_data(dataframe: pd.DataFrame):\n' \
                    f'\ty = dataframe["{label_column_name}"]\n' \
                    f'\tX = dataframe.drop("{label_column_name}", axis=1)\n' \
                    f'\t\n' \
                    f'\tX_train, X_test, y_train, y_test = train_test_split(X, y, test_size={self.__validation_dataset_percentage}, random_state=42)\n' \
                    f'\t\n' \
                    f'\tX_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size={self.__test_dataset_percentage}, random_state=42)\n' \
                    f'\t\n' \
                    f'\treturn X_train.reset_index(drop=True), y_train.reset_index(drop=True), X_val.reset_index(drop=True), y_val.reset_index(drop=True), X_test.reset_index(drop=True), y_test.reset_index(drop=True)\n'
        code += f'\ndataframe: pd.DataFrame = load_dataset()\n'
        code += f'\ncleaned_dataframe = clean_dataset(dataframe)\n'
        code += f'\nX_train, y_train, X_val, y_val, X_test, y_test = split_data(cleaned_dataframe)'
        code += f'\nX_train, y_train, X_val, y_val, X_test, y_test'

        cells.append(Cell(code, CellTypeEnum.CODE))

        return cells
