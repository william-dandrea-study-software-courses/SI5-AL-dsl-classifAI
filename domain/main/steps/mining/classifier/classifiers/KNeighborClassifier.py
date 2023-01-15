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
        pass

    def export(self) -> str:
        pass

    def get_name(self) -> str:
        pass
