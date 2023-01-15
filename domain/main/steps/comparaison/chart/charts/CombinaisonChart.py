from typing import List

from domain.main.steps.comparaison.chart.Chart import Chart
from domain.main.steps.mining.classifier.Classifier import Classifier
from utils.Cell import Cell, CellTypeEnum


class CombinaisonChart(Chart):
    def __init__(self, classifier: Classifier):
        super().__init__()
        self.__classifier: Classifier = classifier

    def export(self) -> List[Cell]:
        return [Cell(f'comparaison_chart({self.__classifier.get_grid_search_name()})\n', CellTypeEnum.CODE)]



