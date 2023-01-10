from abc import ABC
from enum import Enum
from typing import List

from domain.main.steps.mining.hyper_parameter.HyperParameter import HyperParameter


class TrainComparaisonMethodEnum(Enum):
    MEAN_SCORE = "mean_test_score"
    ROC_AUC = "roc_auc"


class Classifier(ABC):
    def __init__(self):
        self.train_comparaison_method: TrainComparaisonMethodEnum = TrainComparaisonMethodEnum.MEAN_SCORE
        self.hyper_parameters: List[HyperParameter] = []

    def set_train_comparaison_method(self, comparaison_method: TrainComparaisonMethodEnum):
        self.train_comparaison_method = comparaison_method
