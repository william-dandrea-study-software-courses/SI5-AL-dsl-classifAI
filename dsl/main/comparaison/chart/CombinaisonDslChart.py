from dsl.main.comparaison.chart.DslChart import DslChart
from dsl.main.mining.classifier.DslClassifier import DslClassifier
from steps.comparaison.chart.charts.CombinaisonChart import CombinaisonChart


class CombinaisonDslChart(DslChart):
    def __init__(self, classifier: DslClassifier):
        super().__init__()
        self.__classifier: DslClassifier = classifier

    def export(self) -> CombinaisonChart:
        chart: CombinaisonChart = CombinaisonChart(self.__classifier.export())
        return chart
