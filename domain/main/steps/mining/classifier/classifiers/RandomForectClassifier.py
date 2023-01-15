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

    def export(self) -> str:
        return f'{self.get_name()} = RandomForestClassifier()\n'

    def get_name(self) -> str:
        return f'random_forest_classifier'

    def get_param_grid(self) -> dict:
        params: dict = {}

        for hp in self._hyper_parameters:

            if not (hp.__class__.__name__ == NEstimatorHP.__name__ or hp.__class__.__name__ == CriterionHP.__name__):
                raise ValueError("Cannot use an hyperparameter that is not available for this classifier")

            if not (hp.get_sklearn_name() in params):
                params[hp.get_sklearn_name()] = []

            if hp.__class__.__name__ == NEstimatorHP.__name__:
                hp: NEstimatorHP = hp
                params[hp.get_sklearn_name()].append(hp.get_n_estimator())

            if hp.__class__.__name__ == CriterionHP.__name__:
                hp: CriterionHP = hp
                params[hp.get_sklearn_name()].append(hp.get_criterion().value)

        return params

