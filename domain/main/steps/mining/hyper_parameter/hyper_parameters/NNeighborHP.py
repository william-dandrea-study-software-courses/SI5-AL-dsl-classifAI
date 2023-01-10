from domain.main.steps import HyperParameter


class NNeighborHP(HyperParameter):

    def __init__(self, n_neighbor: int):
        super().__init__()

        self.n_neighbor: int = n_neighbor
