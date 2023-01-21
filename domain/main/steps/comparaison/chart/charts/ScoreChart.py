from enum import Enum
from typing import List

from domain.main.steps.comparaison.chart.Chart import Chart
from domain.main.steps.mining.classifier.Classifier import Classifier
from utils.Cell import Cell, CellTypeEnum


class ChartScoreEnum(Enum):
    ACCURACY = "accuracy"
    F1_SCORE = "f1_score"
    PRECISION = "precision"
    RECALL = "recall"
    AUC = "auc"


class ScoreChart(Chart):
    def __init__(self):
        super().__init__()
        self.__classifiers: List[Classifier] = []
        self.__scores: List[ChartScoreEnum] = []

    def add_classifier(self, classifier: Classifier):
        self.__classifiers.append(classifier)

    def add_score(self, score: ChartScoreEnum):
        self.__scores.append(score)

    def export(self) -> List[Cell]:

        cells: List[Cell] = []

        code: str = f'scores = {{}}' + '\n'
        code += f'y_test_format = y_test.to_numpy()' + '\n'
        code += f'y_test_format = np.array(np.where(y_test_format == "no", 0, 1), dtype=int)' + '\n'

        for cls in self.__classifiers:

            code += f'prediction = {cls.get_grid_search_name()}.predict(X_test)' + '\n'
            code += f'prediction = np.array(np.where(prediction == "no", 0, 1), dtype=int)' + '\n'
            code += f'scores["{cls.get_name()}"] = {{}}' + '\n'
            code += f'' + '\n'

            for scr in self.__scores:

                method_name: str = ''
                if scr == ChartScoreEnum.F1_SCORE:
                    method_name = "f1_score"
                if scr == ChartScoreEnum.ACCURACY:
                    method_name = "accuracy_score"
                if scr == ChartScoreEnum.PRECISION:
                    method_name = "precision_score"
                if scr == ChartScoreEnum.RECALL:
                    method_name = "recall_score"
                if scr == ChartScoreEnum.AUC:
                    method_name = "roc_auc_score"

                code += f'scores["{cls.get_name()}"]["{scr.value}"] = {method_name}(y_test_format, prediction)' + '\n'
                code += f'' + '\n'



        code += f'plot_df = pd.DataFrame(scores)' + '\n'
        code += f'for cls in {[cls.get_name() for cls in self.__classifiers]}:' + '\n'
        code += f'\tplot_df.plot(y=cls, kind="bar", use_index=True)' + '\n'
        code += f'plot_df' + '\n'

        cells.append(Cell(code, CellTypeEnum.CODE))

        return cells


    def description_charting_infos(self):
        scores = [{
            "name": " / ".join([f"{scr.value}" for scr in self.__scores]),
            "from": [c.get_grid_search_name() for c in self.__classifiers]
        }]


        return [], scores
