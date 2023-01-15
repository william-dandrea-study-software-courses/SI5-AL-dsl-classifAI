from typing import List, Tuple

import nbformat

from steps.preprocessing.Preprocessing import Preprocessing
from steps.splitting.Splitting import Splitting
from utils.Cell import Cell, CellTypeEnum
from utils.Import import Import


class App:

    def __init__(self):
        self.__preprocessing: Preprocessing = None
        self.__splitting: Splitting = None

    def add_preprocessing(self, preprocessing: Preprocessing):
        self.__preprocessing = preprocessing

    def add_splitting(self, splitting: Splitting):
        self.__splitting = splitting


    def generate(self):

        if self.__preprocessing is None:
            raise Exception("Cannot compile code without a preprocessing step")

        if self.__preprocessing is None:
            raise Exception("Cannot compile code without a splitting step")

        # Ajout des imports dans le NoteBook
        imports: List[Import] = self.__preprocessing.get_imports()
        imports += self.__splitting.get_imports()

        # Ajout des cells dans le Notebook
        cells: List[Cell] = self.__preprocessing.export()
        cells += self.__splitting.export()


        nb = nbformat.v4.new_notebook()

        imports_string: str = ""
        for import_value in imports:
            imports_string += f'{import_value.export()}'
        cells.insert(0, Cell(imports_string, CellTypeEnum.CODE))

        for cell in cells:
            nb.cells.append(cell.export())

        return nb
