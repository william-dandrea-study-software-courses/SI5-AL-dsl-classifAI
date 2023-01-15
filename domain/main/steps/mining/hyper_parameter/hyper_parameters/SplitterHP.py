from enum import Enum

from steps.mining.hyper_parameter.HyperParameter import HyperParameter


class SplitterHPEnum(Enum):
    BEST = "best",
    RANDOM = "random"


class SplitterHP(HyperParameter):

    def __init__(self, splitter: SplitterHPEnum):
        super().__init__()

        self.__splitter: SplitterHPEnum = splitter

    def get_sklearn_name(self) -> str:
        return "splitter"

    def get_splitter(self) -> SplitterHPEnum:
        return self.__splitter
