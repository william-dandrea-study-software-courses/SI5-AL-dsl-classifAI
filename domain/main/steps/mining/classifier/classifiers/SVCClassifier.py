from typing import List

from domain.main.steps.mining.classifier.Classifier import Classifier
from steps.mining.hyper_parameter.hyper_parameters.C_HP import C_HP
from utils.Cell import Cell, CellTypeEnum
from utils.Import import Import


class SVCClassifier(Classifier):
    def __init__(self):
        super().__init__()
        self._imports.append(Import("sklearn.svm", "SVC"))

    def add_C(self, C: float):
        self._hyper_parameters.append(C_HP(C))

    def get_name(self) -> str:
        return "svc_classifier"

    def export(self) -> str:
        return f'{self.get_name()} = SVC()\n'

    def get_param_grid(self) -> dict:
        params: dict = {}

        for hp in self._hyper_parameters:

            if not (hp.__class__.__name__ == C_HP.__name__):
                raise ValueError("Cannot use an hyperparameter that is not available for this classifier")

            if not (hp.get_sklearn_name() in params):
                params[hp.get_sklearn_name()] = []

            if hp.__class__.__name__ == C_HP.__name__:
                hp: C_HP = hp
                params[hp.get_sklearn_name()].append(hp.get_C())

        return params

