from enum import Enum

from steps.comparaison.chart.charts.ScoreChart import ChartScoreEnum


class DslChartScoreEnum(Enum):
    F1_SCORE = "F1_SCORE"
    AUC = "AUC"
    RECALL = "RECALL"
    PRECISION = "PRECISION"

    def export(self) -> ChartScoreEnum:
        try:
            return ChartScoreEnum[self.name]
        except KeyError:
            raise ValueError(f"{self.name} is not a valid score")
