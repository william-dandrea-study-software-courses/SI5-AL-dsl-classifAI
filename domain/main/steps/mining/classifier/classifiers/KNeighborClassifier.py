from domain.main.steps.mining.classifier.Classifier import Classifier
from steps.mining.hyper_parameter.hyper_parameters.NNeighborHP import NNeighborHP
from utils.Import import Import


class KNeighborClassifier(Classifier):
    def __init__(self):
        super().__init__()
        self._imports.append(Import("sklearn.neighbors", "KNeighborsClassifier"))

    def add_n_neighbors(self, n_neighbors: int):
        self._hyper_parameters.append(NNeighborHP(n_neighbors))

    def get_param_grid(self) -> dict:

        params: dict = {}

        for hp in self._hyper_parameters:

            if not (hp.__class__.__name__ == NNeighborHP.__name__):
                raise ValueError("Cannot use an hyperparameter that is not available for this classifier")

            if not (hp.get_sklearn_name() in params):
                params[hp.get_sklearn_name()] = []

            if hp.__class__.__name__ == NNeighborHP.__name__:
                hp: NNeighborHP = hp
                params[hp.get_sklearn_name()].append(hp.get_n_neighbor())

        return params

    def export(self) -> str:
        return f'{self.get_name()} = KNeighborsClassifier()\n'

    def get_name(self) -> str:
        return f'k_neighbor_classifier'


