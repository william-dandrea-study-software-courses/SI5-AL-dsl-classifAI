from steps.mining.hyper_parameter.HyperParameter import HyperParameter


class NNeighborHP(HyperParameter):

    def __init__(self, n_neighbor: int):
        super().__init__()

        self.__n_neighbor: int = n_neighbor

    def get_sklearn_name(self) -> str:
        return "n_neighbors"

    def get_n_neighbor(self) -> int:
        return self.__n_neighbor
