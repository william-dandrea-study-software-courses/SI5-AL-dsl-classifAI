from enum import Enum

from domain.main.steps import HyperParameter


class SolverHPEnum(Enum):
    LBFGS = "lbfgs",
    SGD = "sgd",
    ADAM = "adam"


class SolverHP(HyperParameter):

    def __init__(self, solver: SolverHPEnum):
        super().__init__()

        self.solver: SolverHPEnum = solver
