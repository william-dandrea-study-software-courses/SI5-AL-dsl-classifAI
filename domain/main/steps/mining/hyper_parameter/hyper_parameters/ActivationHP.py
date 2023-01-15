from enum import Enum

from steps.mining.hyper_parameter.HyperParameter import HyperParameter


class ActivationHPEnum(Enum):
    IDENTITY = "identity"
    LOGISTIC = "logistic"
    TANH = "tanh"
    RELU = "relu"


class ActivationHP(HyperParameter):

    def __init__(self, activation: ActivationHPEnum):
        super().__init__()

        self.__activation: ActivationHPEnum = activation

    def get_sklearn_name(self) -> str:
        return "activation"

    def get_activation(self) -> ActivationHPEnum:
        return self.__activation
