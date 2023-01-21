import os
import unittest

import nbformat

from dsl.main.DslApp import create_app
from dsl.main.preprocessing.cleaning_methods.DeleteLineDslCleaningMethod import DeleteLineDslCleaningMethod


class MyTestCase(unittest.TestCase):
    def test_something(self):

        my_app = create_app()

        #################
        # Preprocessing #
        #################
        my_app.preprocessing.dataset_file(
            path="dataset.csv",
            is_dataset_contains_header=False
        )

        my_app.preprocessing.dataset.define_qualitative_nominal_col(
            name="color",
            values=["YELLOW", "PURPLE"],
            cleaning_method=DeleteLineDslCleaningMethod(),
            use_default_transformation=True
        )

        my_app.preprocessing.dataset.define_qualitative_ordinal_col(
            name="size",
            values=["SMALL", "LARGE"]
        )
        my_app.preprocessing.dataset.define_qualitative_nominal_col(
            name="act",
            values=["STRETCH", "DIP"]
        )

        my_app.preprocessing.dataset.define_qualitative_nominal_col(
            name="age",
            values=["ADULT", "CHILD"]
        )

        my_app.preprocessing.dataset.define_boolean_col(
            name="result",
            true_value="T",
            false_value="F",
            is_label=True,
        )

        #############
        # Splitting #
        #############
        my_app.splitting.dataset(my_app.preprocessing.dataset)
        my_app.splitting.train_validation_test(
            train_percent=0.6,
            validation_percent=0.2,
            test_percent=0.2
        )

        ##################
        # Transformation #
        ##################

        my_app.transformation.dataset(my_app.preprocessing.dataset)

        ##########
        # Mining #
        ##########

        my_app.mining.train_comparaison_method(method="ACCURACY")

        svc_cls = my_app.mining.svc_classifier() \
            .C(C=[1.0, 2.0])

        decision_tree_cls = my_app.mining.decision_tree_classifier() \
            .splitter(splitter=["BEST", "RANDOM"]) \
            .criterion(criterion=["GINI", "ENTROPY"]) \
            .min_samples_split([10, 12])

        k_neighbor_classifier_cls = my_app.mining.k_neighbor_classifier() \
            .n_neighbors(n_neighbors=[5, 8])

        my_app.mining.mlpc_classifier() \
            .solver(solver=["SGD", "ADAM"]) \
            .activation(activation=["TANH", "IDENTITY"])

        my_app.mining.random_forest_classifier() \
            .criterion(criterion=["GINI", "ENTROPY"]) \
            .n_estimators(n_estimators=[5, 2, 7])

        ###############
        # Comparaison #
        ###############

        my_app.comparaison.add_combinaison_chart(svc_cls)
        my_app.comparaison.add_combinaison_chart(decision_tree_cls)
        my_app.comparaison.add_combinaison_chart(k_neighbor_classifier_cls)

        my_app.comparaison.add_score_chart(scores=["F1_SCORE"], classifiers=[svc_cls, k_neighbor_classifier_cls, decision_tree_cls])

        NAME_OUTPUT: str = 'balloon_notebook.ipynb'

        if os.path.exists(NAME_OUTPUT):
            os.remove(NAME_OUTPUT)

        with open(NAME_OUTPUT, 'w', encoding='utf-8') as f:
            nbformat.write(my_app.generate(), f)





if __name__ == '__main__':
    unittest.main()
