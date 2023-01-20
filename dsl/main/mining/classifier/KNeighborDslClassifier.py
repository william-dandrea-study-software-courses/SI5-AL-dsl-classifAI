from typing import List, cast

from dsl.main.mining.classifier.DslClassifier import DslClassifier
from steps.mining.classifier.classifiers.KNeighborClassifier import KNeighborClassifier


class KNeighborDslClassifier(DslClassifier):

    def __init__(self):
        super().__init__()
        self.__n_neighbors: List[int] = []

    def n_neighbors(self, n_neighbors: List[int]):
        self.__n_neighbors = n_neighbors
        return self

    def export(self) -> KNeighborClassifier:

        if self._classifier is not None:
            return cast(KNeighborClassifier, self._classifier)

        self._classifier: KNeighborClassifier = KNeighborClassifier()

        for n_neighbors in self.__n_neighbors:
            self._classifier.add_n_neighbors(n_neighbors)

        return self._classifier
