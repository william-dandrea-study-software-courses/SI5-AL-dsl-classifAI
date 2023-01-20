from typing import List, cast

from dsl.main.mining.classifier.DslClassifier import DslClassifier
from dsl.main.mining.hyper_parameters.ActivationEnumDslHP import ActivationEnumDslHP
from dsl.main.mining.hyper_parameters.SolverEnumDslHp import SolverEnumDslHp
from steps.mining.classifier.classifiers.MLPCClassifier import MLPCClassifier


class MlpcDslClassifier(DslClassifier):

    def __init__(self):
        super().__init__()
        self.__solver: List[SolverEnumDslHp] = []
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

    def export(self) -> MLPCClassifier:

        if self._classifier is not None:
            return cast(MLPCClassifier, self._classifier)

        self._classifier: MLPCClassifier = MLPCClassifier()

        for solver in self.__solver:
            self._classifier.add_solver(solver.export())

        for activation in self.__activation:
            self._classifier.add_activation(activation.export())

        return self._classifier
