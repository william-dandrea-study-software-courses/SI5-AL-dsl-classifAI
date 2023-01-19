from typing import List

from dsl.main.mining.classifier.DslClassifier import DslClassifier


class SvcDslClassifier(DslClassifier):

    def __init__(self):
        super().__init__()
        self.__C = List[float]

    def C(self, C: List[float]):
        self.__C = C
        return self
