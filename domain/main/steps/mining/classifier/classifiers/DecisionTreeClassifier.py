from domain.main.steps.mining.classifier.Classifier import Classifier
from steps.mining.hyper_parameter.hyper_parameters.CriterionHP import CriterionHP, CriterionHPEnum
from steps.mining.hyper_parameter.hyper_parameters.MinSamplesSplit import MinSamplesPlitHP
from steps.mining.hyper_parameter.hyper_parameters.SplitterHP import SplitterHPEnum, SplitterHP
from utils.Import import Import


class DecisionTreeClassifier(Classifier):
    def __init__(self):
        super().__init__()
        self._imports.append(Import("sklearn.tree", "DecisionTreeClassifier"))

    def add_criterion(self, criterion: CriterionHPEnum):
        self._hyper_parameters.append(CriterionHP(criterion))

    def add_splitter(self, splitter: SplitterHPEnum):
        self._hyper_parameters.append(SplitterHP(splitter))

    def add_min_samples_split(self, min_sample_split: int):
        self._hyper_parameters.append(MinSamplesPlitHP(min_sample_split))



    def get_param_grid(self) -> dict:

        params: dict = {}

        for hp in self._hyper_parameters:

            if not (hp.__class__.__name__ == CriterionHP.__name__ or hp.__class__.__name__ == SplitterHP.__name__ or hp.__class__.__name__ == MinSamplesPlitHP.__name__):
                raise ValueError("Cannot use an hyperparameter that is not available for this classifier")

            if not (hp.get_sklearn_name() in params):
                params[hp.get_sklearn_name()] = []

            if hp.__class__.__name__ == CriterionHP.__name__:
                hp: CriterionHP = hp
                params[hp.get_sklearn_name()].append(hp.get_criterion().value)

            if hp.__class__.__name__ == SplitterHP.__name__:
                hp: SplitterHP = hp
                params[hp.get_sklearn_name()].append(hp.get_splitter().value)

            if hp.__class__.__name__ == MinSamplesPlitHP.__name__:
                hp: MinSamplesPlitHP = hp
                params[hp.get_sklearn_name()].append(hp.get_min_sample_split())

        return params

    def export(self) -> str:
        return f'{self.get_name()} = DecisionTreeClassifier()\n'

    def get_name(self) -> str:
        return "decision_tree_classifier"
