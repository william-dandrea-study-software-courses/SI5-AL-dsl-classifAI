from typing import List, Tuple

import nbformat

from steps.comparaison.Comparaison import Comparaison
from steps.mining.Mining import Mining
from steps.preprocessing.Preprocessing import Preprocessing
from steps.splitting.Splitting import Splitting
from steps.transformation.Transformation import Transformation
from utils.Cell import Cell, CellTypeEnum
from utils.Import import Import


class App:

    def __init__(self):
        self.__preprocessing: Preprocessing = None
        self.__splitting: Splitting = None
        self.__transformation = None
        self.__mining = None
        self.__comparaison = None

    def add_preprocessing(self, preprocessing: Preprocessing):
        self.__preprocessing = preprocessing

    def add_splitting(self, splitting: Splitting):
        self.__splitting = splitting

    def add_transformation(self, transformation: Transformation):
        self.__transformation = transformation

    def add_mining(self, mining: Mining):
        self.__mining = mining

    def add_comparaison(self, comparaison: Comparaison):
        self.__comparaison = comparaison

    def generate(self):

        if self.__preprocessing is None:
            raise Exception("Cannot compile code without a preprocessing step")

        if self.__splitting is None:
            raise Exception("Cannot compile code without a splitting step")

        if self.__transformation is None:
            raise Exception("Cannot compile code without a transformation step")

        if self.__mining is None:
            raise Exception("Cannot compile code without a mining step")

        if self.__comparaison is None:
            raise Exception("Cannot compile code without a comparaison step")

        # Ajout des cells dans le Notebook
        cells: List[Cell] = self.__preprocessing.export()
        cells += self.__splitting.export()
        cells += self.__transformation.export()
        cells += self.__mining.export()
        cells += self.__comparaison.export()

        # Ajout des imports dans le NoteBook
        imports: List[Import] = self.__preprocessing.get_imports()
        imports += self.__splitting.get_imports()
        imports += self.__transformation.get_imports()
        imports += self.__mining.get_imports()
        imports += self.__comparaison.get_imports()

        nb = nbformat.v4.new_notebook()

        imports_string: str = ""
        for import_value in imports:
            imports_string += f'{import_value.export()}'
        cells.insert(0, Cell(imports_string, CellTypeEnum.CODE))

        for cell in cells:
            nb.cells.append(cell.export())

        return nb
