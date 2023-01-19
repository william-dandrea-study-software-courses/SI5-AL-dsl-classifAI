my_app = create_app()

#################
# Preprocessing #
#################

my_app.preprocessing.dataset(path='./breast_cancer.csv')

my_app.preprocessing.data.define_bool_col(
    name='Class',
    true_value='recurrence_events',
    false_value='no_recurrence_events',
    cleaning_method=ReplaceLineCleaningMethod(False)
)

my_app.preprocessing.data.define_bool_col(
    name='node_caps',
    true_value='yes',
    false_value='no',
)

my_app.preprocessing.data.define_bool_col(
    name='irradiat',
    true_value='yes',
    false_value='no',
)

my_app.preprocessing.data.define_quali_ordinal_col(
    name='age',
    possible_values=['10-19', '20-29', '30-39', '40-49',
                     '50-59', '60-69', '70-79', '80-89', '90-99']
)

my_app.preprocessing.data.define_quali_ordinal_col(
    name='tumor_size',
    possible_values=['0-4', '5-9', '10-14', '15-19', '20-24',
                     '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59']
)

my_app.preprocessing.data.define_quali_ordinal_col(
    name='inv_nodes',
    possible_values=['0-2', '3-5', '5-8', '9-11',
                     '12-14', '15-17', '18-20', '21-23', '24-26', '27-29', '30-32', '33-35', '36-39']
)

my_app.preprocessing.data.define_quali_nominal_col(
    name='menopause',
    possible_values=['lt40', 'ge40', 'premeno']
)

my_app.preprocessing.data.define_quali_nominal_col(
    name='breast',
    possible_values=['left', 'right']
)

my_app.preprocessing.data.define_quali_nominal_col(
    name='breast-quad',
    possible_values=['left_up', 'left_low', 'right_up', 'right_low', 'central']
)

my_app.preprocessing.data.define_quanti_discrete_col(
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

my_app.transformation.dataset(my_app.preprocessing.data)


##################
# Mining         #
##################

my_app.classifier.svc_classifier(C=[1.0, 2.0])

my_app.classifier.decision_tree_classifier().splitters(
    ['BEST', 'RANDOM']).criterion(['GINI', 'ENTROPY']).min_sample_split([10, 12])


my_app.classifier.k_neighbor_classifier().n_neighbord([5, 8])

my_app.classifier.mlpc_classifier().solver(
    ['SGD', 'ADAM']).activation(['TANH', 'IDENTITY'])

my_app.classifier.random_forest_classifier().criterion(
    ['GINI', 'ENTROPY']).n_estimators([5, 2])

##################
# Comparaison    #
##################

my_app.comparaison.combinaison_chart(
    my_app.classifier.random_forest_classifier)

my_app.comparaison.score_chart(
    score=[
        ChartScoreEnum.F1_SCORE,
        ChartScoreEnum.AUC,
        ChartScoreEnum.RECALL,
        ChartScoreEnum.PRECISION
    ],
    classifiers=[
        my_app.classifier.svc_classifier,
        my_app.classifier.decision_tree_classifier,
        my_app.classifier.k_neighbor_classifier,
        my_app.mlpc_classifier,
        my_app.classifier.random_forest_classifier
    ]
)
