from domain.main.steps import HyperParameter


class NEstimatorHP(HyperParameter):

    def __init__(self, n_estimator: int):
        super().__init__()

        self.n_estimator: int = n_estimator
