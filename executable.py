from typing import List
from enum import Enum
from sklearn.preprocessing import minmax_scale
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import warnings


import numpy as np
import pandas as pd

warnings.filterwarnings('ignore')



class DataType(Enum):
    BOOLEAN = 1
    QUALITATIVE_NOMINAL = 2         # Named categories : ['FH', 'SF', 'EV']
    QUALITATIVE_ORDINAL = 3         # Categories with an implied order : ['small', 'medium', 'high']
    QUANTITATIVE_DISCRETE = 4       # Only particular numbers : [1, 2, 3, 6, 8]
    QUANTITATIVE_CONTINUOUS = 5     # Any numerical value : [1.345, 2.394, 8.345, 0.432]
    LABEL = 6                       # Label de la classification


class JobWhenMissingValue(Enum):    # Si une valeur d'un dataset est manquante
    DELETE_LINE = 1                 # - On supprime la ligne
    REPLACE_VALUE = 2               # - On remplace la valeur

class EncodingType(Enum):
    ONE_HOT_ENCODER = 1
    ORDINAL_ENCODER = 2



def load_dataset(dataset_url: str, is_csv_file_contains_row_header: bool, names_raw_header: List[str]) -> pd.DataFrame:

    header_value = 1 if is_csv_file_contains_row_header else None
    current_dataset = pd.read_csv(dataset_url, header=header_value)

    if header_value is None:
        current_dataset.columns = names_raw_header

    return current_dataset

def clean_dataset(dataframe: pd.DataFrame, parameters: dict) -> pd.DataFrame:
    """ Méthode qui nettoie le dataset selon les volontés définies par le client dans `parameters`
    :param dataframe: pd.DataFrame = notre dataset
    :param parameters: dict = notre dictionnaire ROWS_DATATYPES
    """
    dataframe = dataframe.replace("?", np.nan)

    for key, value in parameters.items():

        if value["job_when_missing_value"]["type"] == JobWhenMissingValue.DELETE_LINE:
            dataframe = dataframe[dataframe[key].notna()]

        if value["job_when_missing_value"]["type"] == JobWhenMissingValue.REPLACE_VALUE:
            dataframe[key] = dataframe[key].replace(np.nan, value["job_when_missing_value"]["replace_by"])


    return dataframe.reset_index()

def normalize_dataset(dataframe: pd.DataFrame, parameters: dict) -> pd.DataFrame:
    """
    :param dataframe:
    :param parameters:
    :return:
    """
    for key, value in parameters.items():

        if value["datatype"] == DataType.QUANTITATIVE_DISCRETE or value["datatype"] == DataType.QUANTITATIVE_CONTINUOUS:

            dataframe[[key]] = minmax_scale(dataframe[[key]])

    return dataframe

def transform_data(dataframe: pd.DataFrame, parameters: dict) -> pd.DataFrame:
    """
    "datatype": DataType.QUALITATIVE_ORDINAL,
        "possible_values": [ "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90-99" ],
        "encoding": EncodingType.ORDINAL_ENCODER,
        "job_when_missing_value": {
            "type": JobWhenMissingValue.DELETE_LINE,
    }
    """

    for key, value in parameters.items():
        if value["datatype"] == DataType.BOOLEAN:
            remplacement = {
                value["possible_values"][0]: True,
                value["possible_values"][1]: False
            }

            dataframe[key] = dataframe[key].map(remplacement)

        if "encoding" in value and value["encoding"] == EncodingType.ORDINAL_ENCODER:
            # Création de l'objet OrdinalEncoder
            ordinal_encoder = OrdinalEncoder(categories=[value["possible_values"]])

            # Encodage des valeurs de la colonne
            dataframe[key] = ordinal_encoder.fit_transform(dataframe[[key]])

        if "encoding" in value and value["encoding"] == EncodingType.ONE_HOT_ENCODER:
            # Création de l'objet OneHotEncoder
            one_hot_encoder = OneHotEncoder(categories=[value["possible_values"]])

            # Encodage des valeurs de la colonne
            values_encoded = one_hot_encoder.fit_transform(dataframe[[key]]).toarray()

            dataframe = dataframe.drop(key, axis=1)

            dataframe_encoded = pd.DataFrame(values_encoded, columns=[f"{key}_{x}" for x in one_hot_encoder.categories_[0]])
            dataframe = dataframe.join(dataframe_encoded)
    return dataframe


def split_datas(dataframe: pd.DataFrame, parameters: dict):

    label_column_name = None

    for key, value in parameters.items():
        if value["datatype"] == DataType.LABEL:
            label_column_name = key

    if label_column_name is None:
        raise ValueError("Cannot find the label column")

    y = dataframe[label_column_name]
    X = dataframe.drop(label_column_name, axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=42)

    return X_train, y_train, X_val, y_val, X_test, y_test

def generate_scores(scores_to_do: List[str], y, prediction):
    scores = {}
    y_intern = y.to_numpy()
    y_intern = np.array(np.where(y_intern == 'no', 0, 1), dtype=int)
    prediction = np.array(np.where(prediction == 'no', 0, 1), dtype=int)
    for name_score in scores_to_do:
        if name_score == "accuracy":
            scores["accuracy"] = accuracy_score(y_intern, prediction)
        if name_score == "precision":
            scores["precision"] = precision_score(y_intern, prediction)
        if name_score == "recall":
            scores["recall"] = recall_score(y_intern, prediction)
        if name_score == "f1":
            scores["f1"] = f1_score(y_intern, prediction)
        if name_score == "auc":
            scores["auc"] = roc_auc_score(y_intern, prediction)
    return scores

def plot_results(grid_search: GridSearchCV, name_cls, optimizations_values, comparaison_config, X_train, y_train, X_val, y_val, X_test, y_test):

    print("=> ", name_cls)

    # 1. Affichage des résultats sur le set de train
    results = grid_search.cv_results_

    results_dataframe = []
    columns_name = []
    for param, possible_values in optimizations_values.items():
        results_dataframe.append(results[f'param_{param}'].data)
        columns_name.append(f"{param}")
    results_dataframe.append(results['mean_test_score'])
    columns_name.append("mean_test_score")

    results_dataframe = pd.DataFrame(results_dataframe).T
    results_dataframe = results_dataframe.reset_index(drop=True)
    results_dataframe.columns = columns_name
    results_dataframe = results_dataframe.sort_values(by=['mean_test_score'], ascending=False)

    columns_name.remove("mean_test_score")
    # Créez une colonne qui concatène les valeurs de `label_col`
    results_dataframe['combinaison_hyperparameters'] = results_dataframe[columns_name].apply(lambda x: " | ".join(map(str, x)), axis=1)

    fig, ax = plt.subplots(3, 1, figsize=(30, 20))
    ax[0].barh(results_dataframe["combinaison_hyperparameters"], results_dataframe["mean_test_score"], label=name_cls)
    ax[0].set(xlabel='score', ylabel='combinaison de paramètres')
    ax[0].set_title("Résultats de l'entrainement")
    print("====> Train scores", pd.concat([results_dataframe["combinaison_hyperparameters"], results_dataframe["mean_test_score"]], axis=1).set_index('combinaison_hyperparameters')['mean_test_score'].to_dict())

    # 2. Affichage des résultats sur le set de validation
    validation_prediction = grid_search.predict(X_val)
    validations_scores = generate_scores(comparaison_config["validation"], y_val, validation_prediction)
    ax[1].barh(list(validations_scores.keys()), list(validations_scores.values()), label="Validation scores with the best combinaison")
    ax[1].set(xlabel='score', ylabel='type de score')
    ax[1].set_title('Score de validation')
    print("====> Validation scores", validations_scores)


    # 3. Affichage des résultats sur le set de test
    test_prediction = grid_search.predict(X_test)
    test_scores = generate_scores(comparaison_config["test"], y_test, test_prediction)
    ax[2].barh(list(test_scores.keys()), list(test_scores.values()), label="Validation scores with the best combinaison")
    ax[2].set(xlabel='score', ylabel='type de score')
    ax[2].set_title('Score de tests')
    print("====> Tests scores", test_scores)

    plt.show()



def launch_analysis_complete(X_train, y_train, X_val, y_val, X_test, y_test, configuration, comparaison_config):

    for name_cls, optimizations_values in configuration.items():

        clf = None

        if name_cls == "decision_tree":
            clf = DecisionTreeClassifier()

        if name_cls == "random_forest":
            clf = RandomForestClassifier()

        if name_cls == "MLPC":
            clf = MLPClassifier()

        if name_cls == "SVC":
            clf = SVC()

        if name_cls == "k_neighbors":
            clf = KNeighborsClassifier()


        # Initialisez la recherche de grille
        grid_search = GridSearchCV(estimator=clf, param_grid=optimizations_values, cv=5)

        # Entraînez votre modèle en utilisant la recherche de grille
        grid_search.fit(X_train, y_train)

        plot_results(grid_search, name_cls, optimizations_values, comparaison_config, X_train, y_train, X_val, y_val, X_test, y_test)




# Url à partir de la racine du dataset au format CSV
CSV_FILE_URL: str = 'breast-cancer.csv'

# Si le fichier CSV contient les noms de colonnes, mettre à True, si le fichier CSV ne contient
# que les données, et pas les titres, mettre à False
IS_CSV_FILE_CONTAINS_ROW_HEADER: bool = False

# Renommer les noms des colonnes
NAMES_ROWS_HEADER: List[str] = [
    "class",
    "age",
    "menopause",
    "tumor-size",
    "inv-nodes",
    "node-caps",
    "deg-malig",
    "breast",
    "breast-quad",
    "irradiat",
]

# Les types des données qui ont été inséré
ROWS_DATATYPES = {
    "class": {
        "datatype": DataType.BOOLEAN,
        "possible_values": [ "recurrence-events", "no-recurrence-events" ], # TRUE, FALSE
        "job_when_missing_value": {
            "type": JobWhenMissingValue.REPLACE_VALUE,
            "replace_by": False,
        }
    },
    "age": {
        "datatype": DataType.QUALITATIVE_ORDINAL,
        "possible_values": [ "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90-99" ],
        "encoding": EncodingType.ORDINAL_ENCODER,
        "job_when_missing_value": {
            "type": JobWhenMissingValue.DELETE_LINE,
        }
    },
    "menopause": {
        "datatype": DataType.QUALITATIVE_NOMINAL,
        "possible_values": [ "lt40", "premeno", "ge40" ],
        "encoding": EncodingType.ONE_HOT_ENCODER,
        "job_when_missing_value": {
            "type": JobWhenMissingValue.DELETE_LINE,
        }
    },
    "tumor-size": {
        "datatype": DataType.QUALITATIVE_ORDINAL,
        "possible_values": [ "0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59" ],
        "encoding": EncodingType.ORDINAL_ENCODER,
        "job_when_missing_value": {
            "type": JobWhenMissingValue.DELETE_LINE,
        }
    },
    "inv-nodes": {
        "datatype": DataType.QUALITATIVE_ORDINAL,
        "possible_values": [ "0-2", "3-5", "6-8", "9-11", "12-14", "15-17", "18-20", "21-23", "24-26", "27-29", "30-32", "33-35", "36-39" ],
        "encoding": EncodingType.ORDINAL_ENCODER,
        "job_when_missing_value": {
            "type": JobWhenMissingValue.DELETE_LINE,
        }
    },
    "node-caps": {
        "datatype": DataType.BOOLEAN,
        "possible_values": ["yes", "no"],
    },
    "deg-malig": {
        "datatype": DataType.QUANTITATIVE_DISCRETE,
        "job_when_missing_value": {
            "type": JobWhenMissingValue.DELETE_LINE,
        }
    },
    "breast": {
        "datatype": DataType.QUALITATIVE_NOMINAL,
        "possible_values": [ "left", "right" ],
        "encoding": EncodingType.ONE_HOT_ENCODER,
        "job_when_missing_value": {
            "type": JobWhenMissingValue.DELETE_LINE,
        }
    },
    "breast-quad": {
        "datatype": DataType.QUALITATIVE_NOMINAL,
        "possible_values": [ "left_up",  "left_low",  "right_up",  "right_low",  "central" ],
        "encoding": EncodingType.ONE_HOT_ENCODER,
        "job_when_missing_value": {
            "type": JobWhenMissingValue.DELETE_LINE,
        }
    },
    "irradiat": {
        "datatype": DataType.LABEL,
        "possible_values": ["yes", "no"],
        "job_when_missing_value": {
            "type": JobWhenMissingValue.DELETE_LINE,
        }
    },
}

CLASSIFIERS_CONFIGURATION = {
    "decision_tree": {
        "criterion": ["gini", "entropy", "log_loss"],
        "splitter": ["best", "random"],
        "min_samples_split": [2, 3]
    },
    "random_forest": {
        "n_estimators": [100, 200],
        "criterion": ["gini", "entropy", "log_loss"],
    },
    "MLPC": {
        "solver": ['lbfgs', 'sgd', 'adam'],
        "activation" : ['identity', 'logistic', 'tanh', 'relu']
    },
    "SVC": {
        "C": [1.0, 1.5, 2.0]
    },
    "k_neighbors": {
        "n_neighbors": [2, 5, 10]
    }
}

COMPARAISONS_SCORES = {
    "validation": ["accuracy", "precision", "recall", "f1", "auc"],
    "test": ["accuracy", "precision"]
}


current_dataset = load_dataset(CSV_FILE_URL, IS_CSV_FILE_CONTAINS_ROW_HEADER, NAMES_ROWS_HEADER)
current_dataset = clean_dataset(current_dataset, ROWS_DATATYPES)
current_dataset = normalize_dataset(current_dataset, ROWS_DATATYPES)
current_dataset = transform_data(current_dataset, ROWS_DATATYPES)

X_train, y_train, X_val, y_val, X_test, y_test = split_datas(current_dataset, ROWS_DATATYPES)
launch_analysis_complete(X_train, y_train, X_val, y_val, X_test, y_test, CLASSIFIERS_CONFIGURATION, COMPARAISONS_SCORES)
#%%
