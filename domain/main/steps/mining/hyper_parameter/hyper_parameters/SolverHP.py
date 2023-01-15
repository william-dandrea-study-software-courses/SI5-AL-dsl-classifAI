from enum import Enum

from steps.mining.hyper_parameter.HyperParameter import HyperParameter


class SolverHPEnum(Enum):
    LBFGS = "lbfgs"
    SGD = "sgd"
    ADAM = "adam"


class SolverHP(HyperParameter):

    def __init__(self, solver: SolverHPEnum):
        super().__init__()

        self.__solver: SolverHPEnum = solver

    def get_sklearn_name(self) -> str:
        return "solver"

    def get_solver(self) -> SolverHPEnum:
        return self.__solver
