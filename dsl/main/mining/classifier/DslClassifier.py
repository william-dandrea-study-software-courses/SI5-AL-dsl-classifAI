from abc import ABC, abstractmethod

from steps.mining.classifier.Classifier import Classifier


class DslClassifier(ABC):

    def __init__(self):
        self._classifier: Classifier = None

    @abstractmethod
    def export(self) -> Classifier:
        pass
