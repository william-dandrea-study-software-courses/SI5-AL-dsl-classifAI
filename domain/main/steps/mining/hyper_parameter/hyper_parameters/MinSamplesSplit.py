from steps.mining.hyper_parameter.HyperParameter import HyperParameter


class MinSamplesPlitHP(HyperParameter):

    def __init__(self, min_sample_split: int):
        super().__init__()

        self.__min_sample_split: int = min_sample_split

    def get_sklearn_name(self) -> str:
        return "min_samples_split"

    def get_min_sample_split(self) -> int:
        return self.__min_sample_split
