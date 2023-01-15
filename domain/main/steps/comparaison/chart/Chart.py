from abc import ABC, abstractmethod
from typing import List

from utils.Cell import Cell


class Chart(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def export(self) -> List[Cell]:
        pass
