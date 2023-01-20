from typing import List, cast

from dsl.main.mining.classifier.DslClassifier import DslClassifier
from dsl.main.mining.hyper_parameters.CriterionEnumDslHp import CriterionEnumDslHp
from steps.mining.classifier.classifiers.RandomForectClassifier import RandomForestClassifier


class RandomForestDslClassifier(DslClassifier):

    def __init__(self):
        super().__init__()
        self.__criterion: List[CriterionEnumDslHp] = []
        self.__n_estimators: List[int] = []

    def criterion(self, criterion: List[str]):
        self.__criterion = [CriterionEnumDslHp[a] for a in criterion if a in CriterionEnumDslHp.__members__]

        for a in criterion:
            if a not in CriterionEnumDslHp.__members__:
                raise ValueError(f"{a} n'est pas un hyper-paramètre valide")

        return self

    def n_estimators(self, n_estimators: List[int]):
        self.__n_estimators = n_estimators
        return self

    def export(self) -> RandomForestClassifier:

        if self._classifier is not None:
            return cast(RandomForestClassifier, self._classifier)

        self._classifier: RandomForestClassifier = RandomForestClassifier()

        for criterion in self.__criterion:
            self._classifier.add_criterion(criterion.export())

        for n_estimators in self.__n_estimators:
            self._classifier.add_n_estimators(n_estimators)

        return self._classifier
