from dsl.main.comparaison.DslComparaison import DslComparaison
from dsl.main.mining.DslMining import DslMining
from dsl.main.preprocessing.DslPreprocessing import DslPreprocessing
from dsl.main.splitting.DslSplitting import DslSplitting
from dsl.main.transformation.DslTransformation import DslTransformation


class DslApp:

    def __init__(self):
        self.preprocessing = DslPreprocessing()
        self.splitting = DslSplitting()
        self.transformation = DslTransformation()
        self.mining = DslMining()
        self.comparaison = DslComparaison()

    def generate(self):
        pass


def create_app():
    return DslApp()
