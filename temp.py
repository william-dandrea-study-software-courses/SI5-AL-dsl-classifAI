from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class DecisionTree:
    def __init__(self, criterion: str = 'gini', splitter: str = 'best', max_depth: int or float = 'salut', min_samples_split: int or float = 2, min_samples_leaf: int or float = 1, min_weight_fraction_leaf: float = 0.0, max_features: int or float or str = None, random_state: int = None, max_leaf_nodes: int = None, class_weight = None, ccp_alpha: float = 0.0):
        """
        :param criterion: {“gini”, “entropy”, “log_loss”}, default=”gini”
        :param splitter: {“best”, “random”}, default=”best”
        :param max_depth: int, default=None
        :param min_samples_split: int or float, default=2
        :param min_samples_leaf: int or float, default=1
        :param min_weight_fraction_leaf: float, default=0.0
        :param max_features: int, float or {“auto”, “sqrt”, “log2”}, default=None
        :param random_state: int, RandomState instance or None, default=None
        :param max_leaf_nodes: int, default=None
        :param class_weight: dict, list of dict or “balanced”, default=None
        :param ccp_alpha: non-negative float, default=0.0
        """

        self.classifier = DecisionTreeClassifier(criterion=criterion, splitter=splitter, max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf, min_weight_fraction_leaf=min_weight_fraction_leaf, max_features=max_features, random_state=random_state, max_leaf_nodes=max_leaf_nodes, class_weight=class_weight, ccp_alpha=ccp_alpha)


    def get_classifier(self):
        return self.classifier


class RandomForest:
    def __init__(self, n_estimators: int = 100, criterion: str = 'gini', max_depth: int = None, min_samples_split: int or float = 2, min_samples_leaf: int or float = 1, min_weight_fraction_leaf: float = 0.0, max_features = "sqrt", max_leaf_nodes: int = None, min_impurity_decrease: float = 0.0, bootstrap: bool = True, oob_score: bool = False, n_jobs: int = None, random_state = None, verbose: int = 0, warm_start: bool = False, class_weight = None, ccp_alpha: float = 0.0, max_samples = None):
        """
        :param n_estimators: int, default=100
        :param criterion: {“gini”, “entropy”, “log_loss”}, default=”gini”
        :param max_depth: int, default=None
        :param min_samples_split: int or float, default=2
        :param min_samples_leaf: int or float, default=1
        :param min_weight_fraction_leaf: float, default=0.0
        :param max_features: {“sqrt”, “log2”, None}, int or float, default=”sqrt”
        :param max_leaf_nodes: int, default=None
        :param min_impurity_decrease: float, default=0.0
        :param bootstrap: bool, default=True
        :param oob_score: bool, default=False
        :param n_jobs: int, default=None
        :param random_state: int, RandomState instance or None, default=None
        :param verbose: int, default=0
        :param warm_start: bool, default=False
        :param class_weight: {“balanced”, “balanced_subsample”}, dict or list of dicts, default=None
        :param ccp_alpha: non-negative float, default=0.0
        :param max_samples: int or float, default=None
        """

        self.classifier = RandomForestClassifier(n_estimators=n_estimators, criterion=criterion, max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf, min_weight_fraction_leaf=min_weight_fraction_leaf, max_features=max_features, max_leaf_nodes=max_leaf_nodes, min_impurity_decrease=min_impurity_decrease, bootstrap=bootstrap, oob_score=oob_score, n_jobs=n_jobs, random_state=random_state, verbose=verbose, warm_start=warm_start, class_weight=class_weight, ccp_alpha=ccp_alpha, max_samples=max_samples)

    def get_classifier(self):
        return self.classifier


class MLP:
    def __init__(self, hidden_layer_sizes=(100,), activation: str = "relu", solver: str = "adam", alpha: float = 0.0001, batch_size = "auto", learning_rate: str = "constant", learning_rate_init: float = 0.001, power_t: float = 0.5, max_iter: int = 200, shuffle: bool = True, random_state = None, tol: float = 1e-4, verbose: bool = False, warm_start: bool = False, momentum: float = 0.9, nesterovs_momentum: bool = True, early_stopping: bool = False, validation_fraction: float = 0.1, beta_1:  float = 0.9, beta_2: float = 0.999, epsilon: float = 1e-8, n_iter_no_change: int = 10, max_fun: int = 15000):
        """
        hidden_layer_sizes: array-like of shape(n_layers - 2,), default=(100,)
        activation: {‘identity’, ‘logistic’, ‘tanh’, ‘relu’}, default=’relu’
        solver: {‘lbfgs’, ‘sgd’, ‘adam’}, default=’adam’
        alpha: float, default=0.0001
        batch_size: int, default=’auto’
        learning_rate: {‘constant’, ‘invscaling’, ‘adaptive’}, default=’constant’
        learning_rate_init: float, default=0.001
        power_t: float, default=0.5
        max_iter: int, default=200
        shuffle: bool, default=True
        random_state: int, RandomState instance, default=None
        tol: float, default=1e-4
        verbose: bool, default=False
        warm_start: bool, default=False
        momentum: float, default=0.9
        nesterovs_momentum: bool, default=True
        early_stopping: bool, default=False
        validation_fraction: float, default=0.1
        beta_1: float, default=0.9
        beta_2: float, default=0.999
        epsilon: float, default=1e-8
        n_iter_no_change: int, default=10
        max_fun: int, default=15000
        """
        self.classifier = MLPClassifier( hidden_layer_sizes=hidden_layer_sizes, activation=activation, solver=solver, alpha=alpha, batch_size=batch_size, learning_rate=learning_rate, learning_rate_init=learning_rate_init, power_t=power_t, max_iter=max_iter, shuffle=shuffle, random_state=random_state, tol=tol, verbose=verbose, warm_start=warm_start, momentum=momentum, nesterovs_momentum=nesterovs_momentum, early_stopping=early_stopping, validation_fraction=validation_fraction, beta_1=beta_1, beta_2=beta_2, epsilon=epsilon, n_iter_no_change=n_iter_no_change, max_fun=max_fun)

    def get_classifier(self):
        return self.classifier





prediction = grid_search.predict(X_val)
score = accuracy_score(y_val, prediction)
print(f"---------- {score}")

best_score = grid_search.best_score_
print(f'Best score: {best_score:.2f}')


# Récupérez les résultats de la recherche de grille
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
plot_bar_chart(name_cls, results_dataframe, 'mean_test_score', columns_name)
