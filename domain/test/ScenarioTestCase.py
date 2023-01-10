import unittest

import nbformat

from App import App
from steps.preprocessing.Preprocessing import Preprocessing
from utils.dataset.Dataset import Dataset
from utils.dataset.column.BooleanColumn import BooleanColumn
from utils.dataset.column.Column import Column
from utils.dataset.column.qualitative.NominalQualitativeColumn import NominalQualitativeColumn
from utils.dataset.column.qualitative.OrdinalQualitativeColumn import OrdinalQualitativeColumn
from utils.dataset.column.quantitative.DiscreteQuantitativeColumn import DiscreteQuantitativeColumn


class ScenarioTestCase(unittest.TestCase):
    def test_scenario(self):
        # self.assertEqual(True, False)  # add assertion here
        print("Test scenario")

        # ================================================================================== #
        # Instanciation du preprocessing
        # ================================================================================== #
        preprocessing: Preprocessing = Preprocessing(url_dataset="./breast-cancer.csv")

        # ================================================================================== #
        # Instanciation des colonnes
        # ================================================================================== #
        class_column: BooleanColumn = BooleanColumn()
        class_column.set_name("Class")
        class_column.set_true_value("recurrence-events")
        class_column.set_false_value("no-recurrence-events")

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
        node_caps_column.set_false_value("false")

        deg_malig_column: DiscreteQuantitativeColumn() = DiscreteQuantitativeColumn()
        deg_malig_column.set_name("deg-malig")

        breast_column: NominalQualitativeColumn = NominalQualitativeColumn()
        breast_column.set_name("breast")
        breast_column.add_possible_value("left")
        breast_column.add_possible_value("right")

        breast_quad_column: NominalQualitativeColumn = NominalQualitativeColumn()
        breast_quad_column.set_name("breast-quad")
        breast_quad_column.add_possible_value("left-up")
        breast_quad_column.add_possible_value("left-low")
        breast_quad_column.add_possible_value("right-up")
        breast_quad_column.add_possible_value("right-low")
        breast_quad_column.add_possible_value("central")

        irradiat_column: BooleanColumn = BooleanColumn()
        irradiat_column.set_true_value("yes")
        irradiat_column.set_true_value("no")
        irradiat_column.set_is_label()

        # ================================================================================== #
        # Instanciation du dataset
        # ================================================================================== #
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

        # ================================================================================== #
        # Instanciation de l'App
        # ================================================================================== #
        preprocessing.add_dataset(dataset=dataset)
        application: App = App()
        application.add_preprocessing(preprocessing)

        with open('my_notebook.ipynb', 'w', encoding='utf-8') as f:
            nbformat.write(application.generate(), f)


if __name__ == '__main__':
    unittest.main()
