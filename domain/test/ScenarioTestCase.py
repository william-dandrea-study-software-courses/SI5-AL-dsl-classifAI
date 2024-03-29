import unittest

import nbformat

from App import App
from steps.comparaison.Comparaison import Comparaison
from steps.comparaison.chart.charts.CombinaisonChart import CombinaisonChart
from steps.comparaison.chart.charts.ScoreChart import ScoreChart, ChartScoreEnum
from steps.mining.Mining import Mining
from steps.mining.classifier.classifiers.DecisionTreeClassifier import DecisionTreeClassifier
from steps.mining.classifier.classifiers.KNeighborClassifier import KNeighborClassifier
from steps.mining.classifier.classifiers.MLPCClassifier import MLPCClassifier
from steps.mining.classifier.classifiers.RandomForectClassifier import RandomForestClassifier
from steps.mining.classifier.classifiers.SVCClassifier import SVCClassifier
from steps.mining.hyper_parameter.hyper_parameters.ActivationHP import ActivationHPEnum
from steps.mining.hyper_parameter.hyper_parameters.CriterionHP import CriterionHPEnum
from steps.mining.hyper_parameter.hyper_parameters.SolverHP import SolverHPEnum
from steps.mining.hyper_parameter.hyper_parameters.SplitterHP import SplitterHPEnum
from steps.preprocessing.Preprocessing import Preprocessing
from steps.preprocessing.cleaning.DeleteLineCleaningMethod import DeleteLineCleaningMethod
from steps.preprocessing.cleaning.ReplaceLineCleaningMethod import ReplaceLineCleaningMethod
from steps.splitting.Splitting import Splitting
from steps.transformation.Transformation import Transformation
from utils.dataset.Dataset import Dataset
from utils.dataset.column.BooleanColumn import BooleanColumn
from utils.dataset.column.Column import Column
from utils.dataset.column.qualitative.NominalQualitativeColumn import NominalQualitativeColumn
from utils.dataset.column.qualitative.OrdinalQualitativeColumn import OrdinalQualitativeColumn
from utils.dataset.column.quantitative.DiscreteQuantitativeColumn import DiscreteQuantitativeColumn


class ScenarioTestCase(unittest.TestCase):
    def test_scenario(self):

        application: App = App()

        # ================================================================================== #
        # Instanciation du preprocessing
        # ================================================================================== #
        preprocessing: Preprocessing = Preprocessing(url_dataset="./breast-cancer.csv")

        # Instanciation des colonnes
        class_column: BooleanColumn = BooleanColumn()
        class_column.set_name("Class")
        class_column.set_true_value("recurrence-events")
        class_column.set_false_value("no-recurrence-events")
        class_column.set_cleaning_method(ReplaceLineCleaningMethod(False))


        age_column: OrdinalQualitativeColumn = OrdinalQualitativeColumn()
        age_column.set_name("age")
        age_column.add_possible_value("10-19")
        age_column.add_possible_value("20-29")
        age_column.add_possible_value("30-39")
        age_column.add_possible_value("40-49")
        age_column.add_possible_value("50-59")
        age_column.add_possible_value("60-69")
        age_column.add_possible_value("70-79")
        age_column.add_possible_value("80-89")
        age_column.add_possible_value("90-99")
        age_column.set_default_transformation(True)

        menopause_column: NominalQualitativeColumn = NominalQualitativeColumn()
        menopause_column.set_name("menopause")
        menopause_column.add_possible_value("lt40")
        menopause_column.add_possible_value("ge40")
        menopause_column.add_possible_value("premeno")

        tumor_size_column: OrdinalQualitativeColumn = OrdinalQualitativeColumn()
        tumor_size_column.set_name("tumor-size")
        tumor_size_column.add_possible_value("0-4")
        tumor_size_column.add_possible_value("5-9")
        tumor_size_column.add_possible_value("10-14")
        tumor_size_column.add_possible_value("15-19")
        tumor_size_column.add_possible_value("20-24")
        tumor_size_column.add_possible_value("25-29")
        tumor_size_column.add_possible_value("30-34")
        tumor_size_column.add_possible_value("35-39")
        tumor_size_column.add_possible_value("40-44")
        tumor_size_column.add_possible_value("45-49")
        tumor_size_column.add_possible_value("50-54")
        tumor_size_column.add_possible_value("55-59")

        inv_nodes_column: OrdinalQualitativeColumn = OrdinalQualitativeColumn()
        inv_nodes_column.set_name("inv-nodes")
        inv_nodes_column.add_possible_value("0-2")
        inv_nodes_column.add_possible_value("3-5")
        inv_nodes_column.add_possible_value("6-8")
        inv_nodes_column.add_possible_value("9-11")
        inv_nodes_column.add_possible_value("12-14")
        inv_nodes_column.add_possible_value("15-17")
        inv_nodes_column.add_possible_value("18-20")
        inv_nodes_column.add_possible_value("21-23")
        inv_nodes_column.add_possible_value("24-26")
        inv_nodes_column.add_possible_value("27-29")
        inv_nodes_column.add_possible_value("30-32")
        inv_nodes_column.add_possible_value("33-35")
        inv_nodes_column.add_possible_value("36-39")

        node_caps_column: BooleanColumn = BooleanColumn()
        node_caps_column.set_name("node-caps")
        node_caps_column.set_true_value("yes")
        node_caps_column.set_false_value("no")

        deg_malig_column: DiscreteQuantitativeColumn() = DiscreteQuantitativeColumn()
        deg_malig_column.set_name("deg-malig")

        breast_column: NominalQualitativeColumn = NominalQualitativeColumn()
        breast_column.set_name("breast")
        breast_column.add_possible_value("left")
        breast_column.add_possible_value("right")

        breast_quad_column: NominalQualitativeColumn = NominalQualitativeColumn()
        breast_quad_column.set_name("breast-quad")
        breast_quad_column.add_possible_value("left_up")
        breast_quad_column.add_possible_value("left_low")
        breast_quad_column.add_possible_value("right_up")
        breast_quad_column.add_possible_value("right_low")
        breast_quad_column.add_possible_value("central")

        irradiat_column: BooleanColumn = BooleanColumn()
        irradiat_column.set_name("irradiat")
        irradiat_column.set_true_value("yes")
        irradiat_column.set_false_value("no")
        irradiat_column.set_is_label()


        # Instanciation du dataset
        dataset: Dataset = Dataset()
        dataset.add_column(class_column)
        dataset.add_column(age_column)
        dataset.add_column(menopause_column)
        dataset.add_column(tumor_size_column)
        dataset.add_column(inv_nodes_column)
        dataset.add_column(node_caps_column)
        dataset.add_column(deg_malig_column)
        dataset.add_column(breast_column)
        dataset.add_column(breast_quad_column)
        dataset.add_column(irradiat_column)

        # Preprocessing implémentation
        preprocessing.add_dataset(dataset=dataset)

        application.add_preprocessing(preprocessing)

        # ================================================================================== #
        # Splitting
        # ================================================================================== #

        splitting: Splitting = Splitting(dataset=dataset)

        splitting.set_train_dataset_percentage(0.7)
        splitting.set_validation_dataset_percentage(0.15)
        splitting.set_test_dataset_percentage(0.15)

        application.add_splitting(splitting)

        # ================================================================================== #
        # Transformation
        # ================================================================================== #

        transformation: Transformation = Transformation(dataset=dataset)
        application.add_transformation(transformation)

        # ================================================================================== #
        # Mining
        # ================================================================================== #

        mining: Mining = Mining()

        # Création des classifiers
        svc_classifier: SVCClassifier = SVCClassifier()
        svc_classifier.add_C(1.0)
        svc_classifier.add_C(2.0)

        decision_tree_classifier: DecisionTreeClassifier = DecisionTreeClassifier()
        decision_tree_classifier.add_splitter(SplitterHPEnum.BEST)
        decision_tree_classifier.add_splitter(SplitterHPEnum.RANDOM)
        decision_tree_classifier.add_criterion(CriterionHPEnum.GINI)
        decision_tree_classifier.add_criterion(CriterionHPEnum.ENTROPY)
        decision_tree_classifier.add_min_samples_split(10)
        decision_tree_classifier.add_min_samples_split(12)

        k_neighbor_classifier: KNeighborClassifier = KNeighborClassifier()
        k_neighbor_classifier.add_n_neighbors(5)
        k_neighbor_classifier.add_n_neighbors(8)

        mlpc_classifier: MLPCClassifier = MLPCClassifier()
        mlpc_classifier.add_solver(SolverHPEnum.SGD)
        mlpc_classifier.add_solver(SolverHPEnum.ADAM)
        mlpc_classifier.add_activation(ActivationHPEnum.TANH)
        mlpc_classifier.add_activation(ActivationHPEnum.IDENTITY)

        random_forest_classifier: RandomForestClassifier = RandomForestClassifier()
        random_forest_classifier.add_criterion(CriterionHPEnum.GINI)
        random_forest_classifier.add_criterion(CriterionHPEnum.ENTROPY)
        random_forest_classifier.add_n_estimators(5)
        random_forest_classifier.add_n_estimators(2)

        # Ajout des classifiers et mining
        mining.add_classifier(svc_classifier)
        mining.add_classifier(decision_tree_classifier)
        mining.add_classifier(k_neighbor_classifier)
        mining.add_classifier(mlpc_classifier)
        mining.add_classifier(random_forest_classifier)

        application.add_mining(mining)

        # ================================================================================== #
        # Comparaison
        # ================================================================================== #
        comparaison: Comparaison = Comparaison()

        random_forest_classifier_combinaison_chart: CombinaisonChart = CombinaisonChart(random_forest_classifier)
        comparaison.add_chart(random_forest_classifier_combinaison_chart)

        score_chart: ScoreChart = ScoreChart()
        score_chart.add_score(ChartScoreEnum.F1_SCORE)
        score_chart.add_score(ChartScoreEnum.AUC)
        score_chart.add_score(ChartScoreEnum.RECALL)
        score_chart.add_score(ChartScoreEnum.PRECISION)

        score_chart.add_classifier(svc_classifier)
        score_chart.add_classifier(decision_tree_classifier)
        score_chart.add_classifier(k_neighbor_classifier)
        score_chart.add_classifier(mlpc_classifier)
        score_chart.add_classifier(random_forest_classifier)
        comparaison.add_chart(score_chart)

        application.add_comparaison(comparaison)


        with open('my_notebook2.ipynb', 'w', encoding='utf-8') as f:
            nbformat.write(application.generate(), f)


if __name__ == '__main__':
    unittest.main()
