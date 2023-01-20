from typing import List

from dsl.main.comparaison.chart.DslChart import DslChart
from dsl.main.comparaison.chart.DslChartScoreEnum import DslChartScoreEnum
from dsl.main.mining.classifier.DslClassifier import DslClassifier
from steps.comparaison.chart.charts.ScoreChart import ScoreChart


class ScoreDslChart(DslChart):
    def __init__(self, scores: List[str], classifiers: List[DslClassifier]):
        super().__init__()

        self.__classifiers: List[DslClassifier] = classifiers
        self.__scores: List[DslChartScoreEnum] = [DslChartScoreEnum[a] for a in scores if
                                                  a in DslChartScoreEnum.__members__]
        for a in scores:
            if a not in DslChartScoreEnum.__members__:
                raise ValueError(f"{a} n'est pas un hyper-paramètre valide")

    def export(self) -> ScoreChart:
        chart: ScoreChart = ScoreChart()

        for cls in self.__classifiers:
            chart.add_classifier(cls.export())

        for score in self.__scores:
            chart.add_score(score.export())

        return chart
