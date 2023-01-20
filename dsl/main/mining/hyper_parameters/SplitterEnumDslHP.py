from enum import Enum

from steps.mining.hyper_parameter.hyper_parameters.SplitterHP import SplitterHPEnum


class SplitterEnumDslHP(Enum):
    BEST = "BEST"
    RANDOM = "RANDOM"

    def export(self) -> SplitterHPEnum:
        try:
            return SplitterHPEnum[self.name]
        except KeyError:
            raise ValueError(f"{self.name} is not a valid hyperparameter")
