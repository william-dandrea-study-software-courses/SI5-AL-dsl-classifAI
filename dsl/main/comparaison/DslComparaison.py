from typing import List

from dsl.main.DslStep import DslStep
from dsl.main.comparaison.chart.CombinaisonDslChart import CombinaisonDslChart
from dsl.main.comparaison.chart.DslChart import DslChart
from dsl.main.comparaison.chart.DslChartScoreEnum import DslChartScoreEnum
from dsl.main.comparaison.chart.ScoreDslChart import ScoreDslChart
from dsl.main.mining.classifier.DslClassifier import DslClassifier

class DslComparaison(DslStep):
    def __init__(self):
        super().__init__()
        self.__charts: List[DslChart] = []

    def add_combinaison_chart(self, classifier: DslClassifier):
        self.__charts.append(CombinaisonDslChart(classifier))

    def add_score_chart(self, scores: List[str], classifiers: List[DslClassifier]):
        self.__charts.append(ScoreDslChart(scores, classifiers))
