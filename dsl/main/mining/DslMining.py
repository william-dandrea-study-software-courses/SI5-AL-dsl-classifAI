from enum import Enum
from typing import List

from dsl.main.DslStep import DslStep
from dsl.main.mining.classifier.DecisionTreeDslClassifier import DecisionTreeDslClassifier
from dsl.main.mining.classifier.DslClassifier import DslClassifier
from dsl.main.mining.classifier.KNeighborDslClassifier import KNeighborDslClassifier
from dsl.main.mining.classifier.MlpcDslClassifier import MlpcDslClassifier
from dsl.main.mining.classifier.RandomForestDslClassifier import RandomForestDslClassifier
from dsl.main.mining.classifier.SvcDslClassifier import SvcDslClassifier
from steps.mining.Mining import Mining, TrainComparaisonMethodEnum


class TrainComparaisonMethodDslEnum(Enum):
    ACCURACY = "ACCURACY"
    ROC_AUC = "ROC_AUC"

    def export(self) -> TrainComparaisonMethodEnum:
        try:
            return TrainComparaisonMethodEnum[self.name]
        except KeyError:
            raise ValueError(f"{self.name} is not a valid score")


class DslMining(DslStep):

    def __init__(self):
        super().__init__()
        self.__classifiers: List[DslClassifier] = []
        self.__train_comparaison_method: TrainComparaisonMethodDslEnum = TrainComparaisonMethodDslEnum.ACCURACY
        self.__mining: Mining | None = None

    def train_comparaison_method(self, method: str):
        method: List[str] = [method]
        self.__train_comparaison_method = [TrainComparaisonMethodDslEnum[a] for a in method if
                                           a in TrainComparaisonMethodDslEnum.__members__][0]

        for a in method:
            if a not in TrainComparaisonMethodDslEnum.__members__:
                raise ValueError(f"{a} n'est pas un argument valide")

        return self

    def svc_classifier(self) -> SvcDslClassifier:
        classifier: SvcDslClassifier = SvcDslClassifier()
        self.__classifiers.append(classifier)
        return classifier

    def random_forest_classifier(self) -> RandomForestDslClassifier:
        classifier: RandomForestDslClassifier = RandomForestDslClassifier()
        self.__classifiers.append(classifier)
        return classifier

    def mlpc_classifier(self) -> MlpcDslClassifier:
        classifier: MlpcDslClassifier = MlpcDslClassifier()
        self.__classifiers.append(classifier)
        return classifier

    def k_neighbor_classifier(self) -> KNeighborDslClassifier:
        classifier: KNeighborDslClassifier = KNeighborDslClassifier()
        self.__classifiers.append(classifier)
        return classifier

    def decision_tree_classifier(self) -> DecisionTreeDslClassifier:
        classifier: DecisionTreeDslClassifier = DecisionTreeDslClassifier()
        self.__classifiers.append(classifier)
        return classifier

    def export(self) -> Mining:

        if self.__mining is not None:
            return self.__mining

        self.__mining: Mining = Mining()
        self.__mining.set_train_comparaison_method(self.__train_comparaison_method.export())

        for cls in self.__classifiers:
            self.__mining.add_classifier(cls.export())

        return self.__mining
