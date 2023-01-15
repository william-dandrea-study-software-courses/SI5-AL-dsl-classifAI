from steps.mining.hyper_parameter.HyperParameter import HyperParameter


class C_HP(HyperParameter):

    def __init__(self, C: float):
        super().__init__()
        self.__C: float = C

    def get_sklearn_name(self) -> str:
        return "C"

    def get_C(self) -> float:
        return self.__C
