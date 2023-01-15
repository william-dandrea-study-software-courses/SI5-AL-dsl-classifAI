from domain.main.steps.mining.classifier.Classifier import Classifier
from steps.mining.hyper_parameter.hyper_parameters.CriterionHP import CriterionHPEnum, CriterionHP
from steps.mining.hyper_parameter.hyper_parameters.NEstimatorHP import NEstimatorHP
from utils.Import import Import


class RandomForestClassifier(Classifier):
    def __init__(self):
        super().__init__()
        self._imports.append(Import("sklearn.ensemble", "RandomForestClassifier"))

    def add_n_estimators(self, n_estimators: int):
        self._hyper_parameters.append(NEstimatorHP(n_estimators))

    def add_criterion(self, criterion: CriterionHPEnum):
        self._hyper_parameters.append(CriterionHP(criterion))

    def get_param_grid(self) -> dict:
        pass

    def export(self) -> str:
        pass

    def get_name(self) -> str:
        pass
