from domain.main.steps import HyperParameter


class MinSamplesPlitHP(HyperParameter):

    def __init__(self, min_sample_split: int):
        super().__init__()

        self.min_sample_split: int = min_sample_split
