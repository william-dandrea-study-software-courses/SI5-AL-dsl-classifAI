from App import App
from dsl.main.comparaison.DslComparaison import DslComparaison
from dsl.main.mining.DslMining import DslMining
from dsl.main.preprocessing.DslPreprocessing import DslPreprocessing
from dsl.main.splitting.DslSplitting import DslSplitting
from dsl.main.transformation.DslTransformation import DslTransformation


class DslApp:

    def __init__(self):
        self.preprocessing: DslPreprocessing = DslPreprocessing()
        self.splitting: DslSplitting = DslSplitting()
        self.transformation: DslTransformation = DslTransformation()
        self.mining: DslMining = DslMining()
        self.comparaison: DslComparaison = DslComparaison()

        self.__app: App = None

    def generate(self):

        if self.__app is not None:
            return self.__app.generate()

        self.__app: App = App()
        self.__app.add_preprocessing(self.preprocessing.export())
        self.__app.add_splitting(self.splitting.export())
        self.__app.add_transformation(self.transformation.export())
        self.__app.add_mining(self.mining.export())
        self.__app.add_comparaison(self.comparaison.export())
        return self.__app.generate()

def create_app():
    return DslApp()
