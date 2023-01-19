from dsl.main.comparaison.chart.DslChart import DslChart
from dsl.main.mining.classifier.DslClassifier import DslClassifier


class CombinaisonDslChart(DslChart):
    def __init__(self, classifier: DslClassifier):
        self.__classifier: DslClassifier = classifier
        pass
