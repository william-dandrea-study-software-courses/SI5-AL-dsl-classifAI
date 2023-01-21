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
            is_dataset_contains_header=True
        )

        # Categorical;Numerical;Numerical;Categorical;Categorical;Categorical;Categorical;Categorical;Categorical;Categorical;Numerical;Ordinal;Ordinal;Categorical;Categorical;Label 1;Label 2;Label 3;Label 4;Label 5;Label 6;Label 7
        # Motorway;SR;NR;TR;VR;SUR1;SUR2;SUR3;UR;FR;OR;RR;BR;MR;CR;Green frogs;Brown frogs;Common toad;Fire-bellied toad;Tree frog;Common newt;Great crested newt


        my_app.preprocessing.dataset.define_qualitative_nominal_col(
            name="Motorway",
            values=["A1", "S52"]
        )

        my_app.preprocessing.dataset.define_quantitative_discrete_col(
            name="SR",
        )
        my_app.preprocessing.dataset.define_quantitative_discrete_col(
            name="NR",
        )

        my_app.preprocessing.dataset.define_quantitative_discrete_col(
            name="TR",
        )
        my_app.preprocessing.dataset.define_quantitative_discrete_col(
            name="VR",
        )
        my_app.preprocessing.dataset.define_quantitative_discrete_col(
            name="SUR1",
        )
        my_app.preprocessing.dataset.define_quantitative_discrete_col(
            name="SUR2",
        )
        my_app.preprocessing.dataset.define_quantitative_discrete_col(
            name="SUR3",
        )
        my_app.preprocessing.dataset.define_quantitative_discrete_col(
            name="UR",
        )
        my_app.preprocessing.dataset.define_quantitative_discrete_col(
            name="FR",
        )
        my_app.preprocessing.dataset.define_quantitative_discrete_col(
            name="OR",
        )
        my_app.preprocessing.dataset.define_quantitative_discrete_col(
            name="RR",
        )
        my_app.preprocessing.dataset.define_quantitative_discrete_col(
            name="BR",
        )
        my_app.preprocessing.dataset.define_quantitative_discrete_col(
            name="MR",
        )
        my_app.preprocessing.dataset.define_quantitative_discrete_col(
            name="CR",
        )


        my_app.preprocessing.dataset.define_boolean_col(
            name="GreenFrog",
            true_value=1,
            false_value=0,
            is_label=False
        )
        my_app.preprocessing.dataset.define_boolean_col(
            name="BrownFrog",
            true_value=1,
            false_value=0,
            is_label=False
        )
        my_app.preprocessing.dataset.define_boolean_col(
            name="CommonToad",
            true_value=1,
            false_value=0,
            is_label=False
        )
        my_app.preprocessing.dataset.define_boolean_col(
            name="FireBelliedToad",
            true_value=1,
            false_value=0,
            is_label=False
        )
        my_app.preprocessing.dataset.define_boolean_col(
            name="TreeFrog",
            true_value=1,
            false_value=0,
            is_label=False
        )
        my_app.preprocessing.dataset.define_boolean_col(
            name="CommonNewt",
            true_value=1,
            false_value=0,
            is_label=False
        )
        my_app.preprocessing.dataset.define_boolean_col(
            name="greatCreastedNewt",
            true_value=1,
            false_value=0,
            is_label=True
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

        my_app.comparaison.add_score_chart(scores=["PRECISION", "RECALL"], classifiers=[svc_cls, k_neighbor_classifier_cls, decision_tree_cls])

        NAME_OUTPUT: str = 'splitting_notebook.ipynb'

        if os.path.exists(NAME_OUTPUT):
            os.remove(NAME_OUTPUT)

        with open(NAME_OUTPUT, 'w', encoding='utf-8') as f:
            nbformat.write(my_app.generate(), f)



if __name__ == '__main__':
    unittest.main()
