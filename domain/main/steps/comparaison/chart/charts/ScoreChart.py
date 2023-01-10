from enum import Enum
from typing import List

from domain.main.steps.comparaison.chart.Chart import Chart
from domain.main.steps.mining.classifier.Classifier import Classifier


class ChartScoreEnum(Enum):
    ACCURACY = "accuracy",
    F1_SCORE = "f1_score",
    PRECISION = "precision",
    RECALL = "recall",
    AUC = "auc",


class ScoreChart(Chart):
    def __init__(self):
        super().__init__()
        self.classifiers: List[Classifier] = []
        self.scores: List[ChartScoreEnum] = []
