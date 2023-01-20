from enum import Enum

from steps.mining.hyper_parameter.hyper_parameters.SolverHP import SolverHPEnum


class SolverEnumDslHp(Enum):
    LBFGS = "LBFGS"
    SGD = "SGD"
    ADAM = "ADAM"

    def export(self) -> SolverHPEnum:
        try:
            return SolverHPEnum[self.name]
        except KeyError:
            raise ValueError(f"{self.name} is not a valid hyperparameter")

