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

    def generate(self):
        app: App = App()
        app.add_preprocessing(self.preprocessing.export())
        app.add_splitting(self.splitting.export())
        app.add_transformation(self.transformation.export())
        app.add_mining(self.mining.export())
        app.add_comparaison(self.comparaison.export())
        return app.generate()





def create_app():
    return DslApp()
