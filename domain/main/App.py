from typing import List

import nbformat

from steps.preprocessing.Preprocessing import Preprocessing


class App:

    def __init__(self):
        self.preprocessing: Preprocessing = None

    def add_preprocessing(self, preprocessing: Preprocessing):
        self.preprocessing = preprocessing
    def generate(self):

        if self.preprocessing is None:
            raise Exception("Cannot compile code without a preprocessing step")

        preprocessing_cells: List = self.preprocessing.generate()


        nb = nbformat.v4.new_notebook()
        for cell in preprocessing_cells:
            nb.cells.append(cell)

        return nb
