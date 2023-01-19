from enum import Enum


class CriterionEnumDslHp(Enum):
    GINI = "GINI"
    ENTROPY = "ENTROPY"
    LOGLOSS = "LOGLOSS"
