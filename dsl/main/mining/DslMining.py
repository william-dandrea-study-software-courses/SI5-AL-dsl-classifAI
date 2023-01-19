from typing import List

from dsl.main.DslStep import DslStep
from dsl.main.mining.classifier.DecisionTreeDslClassifier import DecisionTreeDslClassifier
from dsl.main.mining.classifier.DslClassifier import DslClassifier
from dsl.main.mining.classifier.KNeighborDslClassifier import KNeighborDslClassifier
from dsl.main.mining.classifier.MlpcDslClassifier import MlpcDslClassifier
from dsl.main.mining.classifier.RandomForestDslClassifier import RandomForestDslClassifier
from dsl.main.mining.classifier.SvcDslClassifier import SvcDslClassifier


class DslMining(DslStep):

    def __init__(self):
        super().__init__()
        self.__classifiers: List[DslClassifier] = []

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
