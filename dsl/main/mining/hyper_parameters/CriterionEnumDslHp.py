from enum import Enum

from steps.mining.hyper_parameter.hyper_parameters.CriterionHP import CriterionHPEnum


class CriterionEnumDslHp(Enum):
    GINI = "GINI"
    ENTROPY = "ENTROPY"
    LOGLOSS = "LOGLOSS"

    def export(self) -> CriterionHPEnum:
        try:
            return CriterionHPEnum[self.name]
        except KeyError:
            raise ValueError(f"{self.name} is not a valid hyperparameter")
