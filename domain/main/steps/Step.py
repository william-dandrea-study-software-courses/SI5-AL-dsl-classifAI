from abc import ABC, abstractmethod
from typing import List

from utils.Cell import Cell
from utils.Import import Import


class Step(ABC):

    def __init__(self):
        self._imports: List[Import] = []

    def get_imports(self) -> List[Import]:
        return self._imports

    @abstractmethod
    def export(self) -> List[Cell]:
        pass
