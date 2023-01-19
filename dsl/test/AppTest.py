import unittest
from enum import Enum

from dsl.main.DslApp import create_app
from steps.preprocessing.cleaning.ReplaceLineCleaningMethod import ReplaceLineCleaningMethod


class MyTestCase(unittest.TestCase):


    def test_launch_app(self):
        my_app = create_app()

        #################
        # Preprocessing #
        #################

        my_app.preprocessing.dataset_file(path='./breast_cancer.csv')

        my_app.preprocessing.dataset.define_boolean_col(
            name='Class',
            true_value='recurrence_events',
            false_value='no_recurrence_events',
            cleaning_method=ReplaceLineCleaningMethod(False),
            use_default_transformation=True
        )

        my_app.preprocessing.dataset.define_boolean_col(
            name='node_caps',
            true_value='yes',
            false_value='no',
        )

        my_app.preprocessing.dataset.define_boolean_col(
            name='irradiat',
            true_value='yes',
            false_value='no',
            is_label=True
        )

        my_app.preprocessing.dataset.define_qualitative_ordinal_col(
            name='age',
            values=['10-19', '20-29', '30-39', '40-49',
                             '50-59', '60-69', '70-79', '80-89', '90-99']
        )

        my_app.preprocessing.dataset.define_qualitative_ordinal_col(
            name='tumor_size',
            values=['0-4', '5-9', '10-14', '15-19', '20-24',
                             '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59']
        )

        my_app.preprocessing.dataset.define_qualitative_ordinal_col(
            name='inv_nodes',
            values=['0-2', '3-5', '5-8', '9-11',
                             '12-14', '15-17', '18-20', '21-23', '24-26', '27-29', '30-32', '33-35', '36-39']
        )

        my_app.preprocessing.dataset.define_qualitative_nominal_col(
            name='menopause',
            values=['lt40', 'ge40', 'premeno']
        )

        my_app.preprocessing.dataset.define_qualitative_nominal_col(
            name='breast',
            values=['left', 'right']
        )

        my_app.preprocessing.dataset.define_qualitative_nominal_col(
            name='breast-quad',
            values=['left_up', 'left_low', 'right_up', 'right_low', 'central']
        )

        my_app.preprocessing.dataset.define_quantitative_discrete_col(
            name="deg-malig"
        )

        #############
        # Splitting #
        #############

        my_app.splitting.train_validation_test(
            train_percent=0.7,
            validation_percent=0.15,
            test_percent=0.15
        )

        ##################
        # Transformation #
        ##################

        my_app.transformation.dataset(my_app.preprocessing.dataset)

        ##########
        # Mining #
        ##########

        svc_cls = my_app.mining.svc_classifier()\
            .C(C=[1.0, 2.0])

        decision_tree_cls = my_app.mining.decision_tree_classifier()\
            .splitter(splitter=["BEST", "RANDOM"])\
            .criterion(criterion=["GINI", "ENTROPY"])\
            .min_samples_split([10, 12])

        my_app.mining.k_neighbor_classifier()\
            .n_neighbors(n_neighbors=[5, 8])

        my_app.mining.mlpc_classifier()\
            .solver(solver=["SGD", "ADAM"])\
            .activation(activation=["TANH", "IDENTITY"])

        my_app.mining.random_forest_classifier()\
            .criterion(criterion=["GINI", "ENTROPY"])\
            .n_estimators(n_estimators=[5, 2])

        ###############
        # Comparaison #
        ###############

        my_app.comparaison.add_combinaison_chart(svc_cls)
        my_app.comparaison.add_combinaison_chart(decision_tree_cls)

        my_app.comparaison.add_score_chart(scores=["F1_SCORE", "AUC"], classifiers=[svc_cls, decision_tree_cls])





if __name__ == '__main__':
    unittest.main()
