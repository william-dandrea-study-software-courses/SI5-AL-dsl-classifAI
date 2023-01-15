from domain.main.steps.mining.classifier.Classifier import Classifier
from steps.mining.hyper_parameter.hyper_parameters.ActivationHP import ActivationHPEnum, ActivationHP
from steps.mining.hyper_parameter.hyper_parameters.SolverHP import SolverHP, SolverHPEnum
from utils.Import import Import


class MLPCClassifier(Classifier):
    def __init__(self):
        super().__init__()
        self._imports.append(Import("sklearn.neural_network", "MLPClassifier"))

    def add_solver(self, solver: SolverHPEnum):
        self._hyper_parameters.append(SolverHP(solver))

    def add_activation(self, activation: ActivationHPEnum):
        self._hyper_parameters.append(ActivationHP(activation))

    def get_param_grid(self) -> dict:
        params: dict = {}

        for hp in self._hyper_parameters:

            if not (hp.__class__.__name__ == SolverHP.__name__ or hp.__class__.__name__ == ActivationHP.__name__):
                raise ValueError("Cannot use an hyperparameter that is not available for this classifier")

            if not (hp.get_sklearn_name() in params):
                params[hp.get_sklearn_name()] = []

            if hp.__class__.__name__ == SolverHP.__name__:
                hp: SolverHP = hp
                params[hp.get_sklearn_name()].append(hp.get_solver().value)

            if hp.__class__.__name__ == ActivationHP.__name__:
                hp: ActivationHP = hp
                params[hp.get_sklearn_name()].append(hp.get_activation().value)

        return params

    def export(self) -> str:
        return f'{self.get_name()} = MLPClassifier()\n'


    def get_name(self) -> str:
        return 'mlp_classifier'



