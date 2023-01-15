from steps.mining.hyper_parameter.HyperParameter import HyperParameter


class NEstimatorHP(HyperParameter):

    def __init__(self, n_estimator: int):
        super().__init__()

        self.__n_estimator: int = n_estimator

    def get_sklearn_name(self) -> str:
        return "n_estimators"

    def get_n_estimator(self) -> int:
        return self.__n_estimator
