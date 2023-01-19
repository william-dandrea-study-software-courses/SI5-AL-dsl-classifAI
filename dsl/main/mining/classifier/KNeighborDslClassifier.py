from typing import List

from dsl.main.mining.classifier.DslClassifier import DslClassifier


class KNeighborDslClassifier(DslClassifier):

    def __init__(self):
        super().__init__()
        self.__n_neighbors: List[int] = []

    def n_neighbors(self, n_neighbors: List[int]):
        self.__n_neighbors = n_neighbors
        return self
