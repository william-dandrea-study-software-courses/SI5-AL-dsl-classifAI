from enum import Enum

from domain.main.steps import HyperParameter


class SplitterHPEnum(Enum):
    BEST = "best",
    RANDOM = "random"


class SplitterHP(HyperParameter):

    def __init__(self, splitter: SplitterHPEnum):
        super().__init__()

        self.splitter: SplitterHPEnum = splitter
