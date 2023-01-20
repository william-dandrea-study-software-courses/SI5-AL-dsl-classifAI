from typing import List, cast

from dsl.main.mining.classifier.DslClassifier import DslClassifier
from steps.mining.classifier.classifiers.SVCClassifier import SVCClassifier


class SvcDslClassifier(DslClassifier):

    def __init__(self):
        super().__init__()
        self.__C: List[float] = []

    def C(self, C: List[float]):
        self.__C = C
        return self

    def export(self) -> SVCClassifier:

        if self._classifier is not None:
            return cast(SVCClassifier, self._classifier)

        self._classifier: SVCClassifier = SVCClassifier()

        for c_val in self.__C:
            self._classifier.add_C(c_val)

        return self._classifier
