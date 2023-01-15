from enum import Enum

from steps.mining.hyper_parameter.HyperParameter import HyperParameter


class CriterionHPEnum(Enum):
    GINI = "gini"
    ENTROPY = "entropy"
    LOGLOSS = "logloss"


class CriterionHP(HyperParameter):

    def __init__(self, criterion: CriterionHPEnum):
        super().__init__()

        self.__criterion: CriterionHPEnum = criterion

    def get_sklearn_name(self) -> str:
        return "criterion"

    def get_criterion(self) -> CriterionHPEnum:
        return self.__criterion
