from enum import Enum


class DslChartScoreEnum(Enum):
    F1_SCORE = "F1_SCORE"
    AUC = "AUC"
    RECALL = "RECALL"
    PRECISION = "PRECISION"
