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
        pass

    def export(self) -> str:
        pass

    def get_name(self) -> str:
        pass
