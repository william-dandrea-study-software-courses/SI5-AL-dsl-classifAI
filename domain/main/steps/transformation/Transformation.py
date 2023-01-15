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
            if column.get_default_transformation():
                if column.__class__.__name__ == BooleanColumn.__name__:
                    bool_column: BooleanColumn = column

                    if not bool_column.get_is_label():
                        replacement = { bool_column.get_true_value(): True, bool_column.get_false_value(): False }
                        code_cell += f'\tX_train["{column.get_name()}"] = X_train["{column.get_name()}"].map({replacement})\n' \
                                     f'\tX_val["{column.get_name()}"] = X_val["{column.get_name()}"].map({replacement})\n' \
                                     f'\tX_test["{column.get_name()}"] = X_test["{column.get_name()}"].map({replacement})\n' \
                                     f'\t\n'


                if column.__class__.__name__ == ContinuousQuantitativeColumn.__name__:
                    code_cell += f'\tX_train["{column.get_name()}"] = X_train["{column.get_name()}"].astype(float) \n' \
                                 f'\tX_val["{column.get_name()}"] = X_val["{column.get_name()}"].astype(float) \n' \
                                 f'\tX_test["{column.get_name()}"] = X_test["{column.get_name()}"].astype(float) \n' \
                                 f'\tX_train[["{column.get_name()}"]] = minmax_scale(X_train[["{column.get_name()}"]]) \n' \
                                 f'\tX_val[["{column.get_name()}"]] = minmax_scale(X_val[["{column.get_name()}"]])\n' \
                                 f'\tX_test[["{column.get_name()}"]] = minmax_scale(X_test[["{column.get_name()}"]])\n' \
                                 f'\t\n'

                if column.__class__.__name__ == DiscreteQuantitativeColumn.__name__:
                    code_cell += f'\tX_train["{column.get_name()}"] = X_train["{column.get_name()}"].astype(float) \n' \
                                 f'\tX_val["{column.get_name()}"] = X_val["{column.get_name()}"].astype(float) \n' \
                                 f'\tX_test["{column.get_name()}"] = X_test["{column.get_name()}"].astype(float) \n' \
                                 f'\tX_train[["{column.get_name()}"]] = minmax_scale(X_train[["{column.get_name()}"]]) \n' \
                                 f'\tX_val[["{column.get_name()}"]] = minmax_scale(X_val[["{column.get_name()}"]])\n' \
                                 f'\tX_test[["{column.get_name()}"]] = minmax_scale(X_test[["{column.get_name()}"]])\n' \
                                 f'\t\n'

                if column.__class__.__name__ == NominalQualitativeColumn.__name__:
                    nom_column: NominalQualitativeColumn = column
                    code_cell += f'\tone_hot_encoder = OneHotEncoder( categories=[{nom_column.get_possible_values()}])\n' \
                                 f'\tX_train_encoded_values = one_hot_encoder.fit_transform(X_train[["{nom_column.get_name()}"]]).toarray()\n' \
                                 f'\tX_val_encoded_values = one_hot_encoder.fit_transform(X_val[["{nom_column.get_name()}"]]).toarray()\n' \
                                 f'\tX_test_encoded_values = one_hot_encoder.fit_transform(X_test[["{nom_column.get_name()}"]]).toarray()\n' \
                                 f'\t\n' \
                                 f'\t\n' \
                                 f'\tX_train_encoded = pd.DataFrame(X_train_encoded_values, columns=[f"{nom_column.get_name()}_{{x}}" for x in one_hot_encoder.categories_[0]])\n' \
                                 f'\tX_val_encoded = pd.DataFrame(X_val_encoded_values, columns=[f"{nom_column.get_name()}_{{x}}" for x in one_hot_encoder.categories_[0]])\n' \
                                 f'\tX_test_encoded = pd.DataFrame(X_test_encoded_values, columns=[f"{nom_column.get_name()}_{{x}}" for x in one_hot_encoder.categories_[0]])\n' \
                                 f'\tX_train = X_train.join(X_train_encoded)\n' \
                                 f'\tX_val = X_val.join(X_val_encoded)\n' \
                                 f'\tX_test = X_test.join(X_test_encoded)\n' \
                                 f'\t\n' \
                                 f'\tX_train = X_train.drop("{column.get_name()}", axis=1)\n' \
                                 f'\tX_val = X_val.drop("{column.get_name()}", axis=1)\n' \
                                 f'\tX_test = X_test.drop("{column.get_name()}", axis=1)\n' \
                        # pd.concat([X_train, X_val, X_test], axis=1).to_csv("tst.csv")

                # f'\tX_train = X_train.drop("{column.get_name()}", axis=1)\n' \
                # f'\tX_val = X_val.drop("{column.get_name()}", axis=1)\n' \
                # f'\tX_test = X_test.drop("{column.get_name()}", axis=1)\n' \
                if column.__class__.__name__ == OrdinalQualitativeColumn.__name__:
                    ord_column: OrdinalQualitativeColumn = column
                    code_cell += f'\tordinal_encoder = OrdinalEncoder(categories=[{ord_column.get_possible_values()}])\n' \
                                 f'\tX_train["{column.get_name()}"] = ordinal_encoder.fit_transform(X_train[["{column.get_name()}"]])\n' \
                                 f'\tX_val["{column.get_name()}"] = ordinal_encoder.fit_transform(X_val[["{column.get_name()}"]])\n' \
                                 f'\tX_test["{column.get_name()}"] = ordinal_encoder.fit_transform(X_test[["{column.get_name()}"]])\n' \
                                 f'\t\n'

        code_cell += f'\treturn X_train, X_val, X_test\n'

        code_cell += f'\ndataframe: pd.DataFrame = load_dataset()\n'
        code_cell += f'cleaned_dataframe = clean_dataset(dataframe)\n'
        code_cell += f'X_train, y_train, X_val, y_val, X_test, y_test = split_data(cleaned_dataframe)\n'
        code_cell += f'X_train, X_val, X_test = transform_data(X_train, X_val, X_test)\n'
        code_cell += f'X_train\n'

        cells.append(Cell(code_cell, CellTypeEnum.CODE))

        return cells
