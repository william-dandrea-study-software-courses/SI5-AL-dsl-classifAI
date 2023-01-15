from abc import ABC, abstractmethod
from enum import Enum
from typing import List

from domain.main.steps.mining.hyper_parameter.HyperParameter import HyperParameter
from utils.Import import Import


class Classifier(ABC):
    def __init__(self):
        self._hyper_parameters: List[HyperParameter] = []
        self._imports: List[Import] = []

    def get_imports(self) -> List[Import]:
        return self._imports

    def get_grid_search_name(self) -> str:
        return f'grid_search_{self.get_name()}'

    @abstractmethod
    def get_param_grid(self) -> dict:
        pass

    @abstractmethod
    def export(self) -> str:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass
