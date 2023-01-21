from typing import List

from domain.main.steps.Step import Step
from steps.comparaison.chart.Chart import Chart
from utils.Cell import Cell, CellTypeEnum
from utils.Import import Import


class Comparaison(Step):

    def __init__(self):
        super().__init__()
        self._imports.append(Import("matplotlib.pyplot", None, "plt"))
        self._imports.append(Import("sklearn.metrics", "accuracy_score, precision_score, recall_score, f1_score, roc_auc_score"))

        self.__charts: List[Chart] = []

    def add_chart(self, chart: Chart):
        self.__charts.append(chart)

    def export(self) -> List[Cell]:
        cells: List[Cell] = [Cell("# Comparaison", CellTypeEnum.MARKDOWN)]

        cells.append(Cell(self.__comparaison_chart_export(), CellTypeEnum.CODE))

        for chart in self.__charts:
            cells += chart.export()

        return cells

    def get_description_charting_infos(self):
        description_infos_comparaison = []
        description_infos_score = []
        for chart in self.__charts:
            dsr_cpr, dsr_scr = chart.description_charting_infos()
            description_infos_comparaison += dsr_cpr
            description_infos_score += dsr_scr

        return description_infos_comparaison, description_infos_score



    def __comparaison_chart_export(self) -> str:
        code: str = f'def comparaison_chart(grid_search_name):' + '\n'
        code += f'\tresults = grid_search_name.cv_results_' + '\n'
        code += f'\tparams = results["params"]' + '\n'
        code += f'\tmean_tst_scores = results["mean_test_score"]' + '\n'
        code += f'\tfor index, p in enumerate(params):' + '\n'
        code += f'\t\tp["mean_test_score"] = mean_tst_scores[index]' + '\n'
        code += f'\tresults_dataframe = pd.DataFrame(params)' + '\n'
        code += f'\t' + '\n'
        code += f'\tcolumns_name = results_dataframe.columns.to_list()' + '\n'
        code += f'\tresults_dataframe = results_dataframe.sort_values(by=["mean_test_score"], ascending=False)' + '\n'
        code += f'\tcolumns_name.remove("mean_test_score")' + '\n'
        code += f'\tresults_dataframe["combinaison_hyperparameters"] = results_dataframe[columns_name].apply(lambda x: " | ".join(map(str, x)), axis=1)' + '\n'
        code += f'\t' + '\n'
        code += f'\t' + '\n'
        code += f'\tplt.barh(results_dataframe["combinaison_hyperparameters"], results_dataframe["mean_test_score"])' + '\n'
        code += f'\tplt.xlabel = "score"' + '\n'
        code += f'\tplt.ylabel = "combinaison de paramètres"' + '\n'
        code += f'\tplt.title = "Résultats d entrainement"' + '\n'
        code += f'\tplt.plot()' + '\n'

        return code
