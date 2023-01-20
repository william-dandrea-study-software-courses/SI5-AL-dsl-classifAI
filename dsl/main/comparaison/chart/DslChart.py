from abc import ABC, abstractmethod

from steps.comparaison.chart.Chart import Chart


class DslChart(ABC):
    def __init__(self):
        pass


    @abstractmethod
    def export(self) -> Chart:
        pass
