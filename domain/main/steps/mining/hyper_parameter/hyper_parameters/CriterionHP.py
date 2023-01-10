from enum import Enum

from domain.main.steps import HyperParameter


class CriterionHPEnum(Enum):
    GINI = "gini",
    ENTROPY = "entropy",
    LOGLOSS = "logloss"


class CriterionHP(HyperParameter):

    def __init__(self, criterion: CriterionHPEnum):
        super().__init__()

        self.criterion: CriterionHPEnum = criterion
