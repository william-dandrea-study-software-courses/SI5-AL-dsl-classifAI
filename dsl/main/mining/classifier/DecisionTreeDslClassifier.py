from typing import List, cast

from dsl.main.mining.classifier.DslClassifier import DslClassifier
from dsl.main.mining.hyper_parameters.CriterionEnumDslHp import CriterionEnumDslHp
from dsl.main.mining.hyper_parameters.SplitterEnumDslHP import SplitterEnumDslHP
from steps.mining.classifier.classifiers.DecisionTreeClassifier import DecisionTreeClassifier


class DecisionTreeDslClassifier(DslClassifier):

    def __init__(self):
        super().__init__()
        self.__splitter: List[SplitterEnumDslHP] = []
        self.__min_samples_split: List[int] = []
        self.__criterion: List[CriterionEnumDslHp] = []

    def splitter(self, splitter: List[str]):
        self.__splitter = [SplitterEnumDslHP[a] for a in splitter if a in SplitterEnumDslHP.__members__]

        for a in splitter:
            if a not in SplitterEnumDslHP.__members__:
                raise ValueError(f"{a} n'est pas un hyper-paramètre valide")

        return self

    def criterion(self, criterion: List[str]):
        self.__criterion = [CriterionEnumDslHp[a] for a in criterion if a in CriterionEnumDslHp.__members__]

        for a in criterion:
            if a not in CriterionEnumDslHp.__members__:
                raise ValueError(f"{a} n'est pas un hyper-paramètre valide")

        return self

    def min_samples_split(self, min_samples_split: List[int]):
        self.__min_samples_split: List[int] = min_samples_split
        return self


    def export(self) -> DecisionTreeClassifier:

        if self._classifier is not None:
            return cast(DecisionTreeClassifier, self._classifier)

        self._classifier: DecisionTreeClassifier = DecisionTreeClassifier()

        for splitter in self.__splitter:
            self._classifier.add_splitter(splitter.export())

        for criterion in self.__criterion:
            self._classifier.add_criterion(criterion.export())

        for min_samples_split in self.__min_samples_split:
            self._classifier.add_min_samples_split(min_samples_split)

        return self._classifier
