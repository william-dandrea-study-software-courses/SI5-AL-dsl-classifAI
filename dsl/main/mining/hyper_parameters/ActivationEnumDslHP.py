from enum import Enum

from steps.mining.hyper_parameter.hyper_parameters.ActivationHP import ActivationHPEnum


class ActivationEnumDslHP(Enum):
    IDENTITY = "IDENTITY"
    LOGISTIC = "LOGISTIC"
    TANH = "TANH"
    RELU = "RELU"

    def export(self) -> ActivationHPEnum:
        try:
            return ActivationHPEnum[self.name]
        except KeyError:
            raise ValueError(f"{self.name} is not a valid hyperparameter")
