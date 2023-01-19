from typing import List

from dsl.main.mining.classifier.DslClassifier import DslClassifier
from dsl.main.mining.hyper_parameters.ActivationEnumDslHP import ActivationEnumDslHP
from dsl.main.mining.hyper_parameters.SolverEnumDslHp import SolverEnumDslHp


class MlpcDslClassifier(DslClassifier):

    def __init__(self):
        super().__init__()
        self.__solver: List[str] = []
        self.__activation: List[ActivationEnumDslHP] = []

    def solver(self, solver: List[str]):
        self.__solver = [SolverEnumDslHp[a] for a in solver if a in SolverEnumDslHp.__members__]

        for a in solver:
            if a not in SolverEnumDslHp.__members__:
                raise ValueError(f"{a} n'est pas un hyper-paramètre valide")

        return self

    def activation(self, activation: List[str]):
        self.__activation = [ActivationEnumDslHP[a] for a in activation if a in ActivationEnumDslHP.__members__]

        for a in activation:
            if a not in ActivationEnumDslHP.__members__:
                raise ValueError(f"{a} n'est pas un hyper-paramètre valide")

        return self
