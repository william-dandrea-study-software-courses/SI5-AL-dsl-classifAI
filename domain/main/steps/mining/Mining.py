from enum import Enum
from typing import List

from domain.main.steps.Step import Step
from steps.mining.classifier.Classifier import Classifier
from utils.Cell import Cell, CellTypeEnum
from utils.Import import Import


class TrainComparaisonMethodEnum(Enum):
    ACCURACY = "accuracy"
    ROC_AUC = "roc_auc"


class Mining(Step):

    def __init__(self):
        super().__init__()
        self.__classifiers: List[Classifier] = []
        self.__train_comparaison_method: TrainComparaisonMethodEnum = TrainComparaisonMethodEnum.ACCURACY
        self._imports.append(Import("sklearn.model_selection", "GridSearchCV"))
        self._imports.append(Import("sklearn.model_selection", "PredefinedSplit"))

    def set_train_comparaison_method(self, comparaison_method: TrainComparaisonMethodEnum):
        self.__train_comparaison_method = comparaison_method

    def add_classifier(self, classifier: Classifier):
        self.__classifiers.append(classifier)

    def export(self) -> List[Cell]:

        cells: List[Cell] = [Cell("# Mining", CellTypeEnum.MARKDOWN)]

        for cls in self.__classifiers:
            code: str = ''

            self._imports += cls.get_imports()
            code += cls.export() + '\n'
            code += f'split = [-1 if i < len(X_train) else 0 for i in range(X_train.shape[0] + X_val.shape[0])]' + '\n'
            code += f'grid_search_{cls.get_name()} = GridSearchCV(estimator={cls.get_name()}, param_grid={cls.get_param_grid()}, scoring="{self.__train_comparaison_method.value}", cv=PredefinedSplit(split), verbose=2)' + '\n'
            code += f'grid_search_{cls.get_name()}.fit(np.concatenate([X_train, X_val]), np.concatenate([y_train, y_val]))' + '\n'

            code += f'grid_search_{cls.get_name()}.best_params_'

            cells.append(Cell(code, CellTypeEnum.CODE))

        return cells
