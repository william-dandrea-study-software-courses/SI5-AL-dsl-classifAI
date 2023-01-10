from typing import List

from domain.main.steps.comparaison.chart.Chart import Chart
from domain.main.steps.mining.classifier.Classifier import Classifier


class CombinaisonChart(Chart):
    def __init__(self):
        super().__init__()
        self.classifiers: List[Classifier] = []
