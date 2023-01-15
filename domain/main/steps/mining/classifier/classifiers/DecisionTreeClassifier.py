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
        pass

    def export(self) -> str:
        pass

    def get_name(self) -> str:
        pass
