from enum import Enum

from domain.main.steps import HyperParameter


class ActivationHPEnum(Enum):
    IDENTITY = "identity",
    LOGISTIC = "logistic",
    TANH = "tanh",
    RELU = "relu"


class ActivationHP(HyperParameter):

    def __init__(self, activation: ActivationHPEnum):
        super().__init__()

        self.activation: ActivationHPEnum = activation
