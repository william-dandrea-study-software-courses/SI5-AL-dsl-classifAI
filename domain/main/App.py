from typing import List, Tuple

import nbformat
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

from steps.comparaison.Comparaison import Comparaison
from steps.mining.Mining import Mining
from steps.preprocessing.Preprocessing import Preprocessing
from steps.splitting.Splitting import Splitting
from steps.transformation.Transformation import Transformation
from utils.Cell import Cell, CellTypeEnum
from utils.Import import Import

import warnings


class App:

    def __init__(self):
        self.__preprocessing: Preprocessing = None
        self.__splitting: Splitting = None
        self.__transformation: Transformation = None
        self.__mining: Mining = None
        self.__comparaison: Comparaison = None

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

        try:
            self.__create_mindmap_image()
        except:
            warnings.warn("Cannot generate the mindmap image")

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

    def __create_mindmap_image(self):

        classifiers_arr = []

        comparaisons_charts, scores_charts = self.__comparaison.get_description_charting_infos()
        # [self.__classifier.get_grid_search_name()], [{
        #             "name": " / ".join([f"{scr.value}" for scr in self.__scores]),
        #             "from": [c.get_grid_search_name() for c in self.__classifiers]
        #         }]

        for cls in self.__mining.get_classifiers():
            classifiers_arr.append(
                {
                    "name": cls.get_grid_search_name(),
                    "comparaison": cls.get_grid_search_name() in comparaisons_charts
                }
            )

        scores = scores_charts
        X_START = 8

        new_labels = {}
        new_positions = {}
        new_edges = []

        max_val = X_START + len(classifiers_arr) - 1
        pos_y_cls = 10
        for index, cls in enumerate(classifiers_arr):
            new_labels[X_START + index] = cls["name"]
            cls["index"] = X_START + index
            new_edges += [(5, X_START + index), (6, X_START + index)]
            new_positions[X_START + index] = (100, pos_y_cls)

            if cls["comparaison"]:
                new_labels[X_START + len(classifiers_arr) + index] = f"{cls['name']}_comparaison_{index}"
                new_positions[X_START + len(classifiers_arr) + index] = (150, pos_y_cls)
                new_edges += [(X_START + index, X_START + len(classifiers_arr) + index),
                              (X_START + index, X_START + len(classifiers_arr) + index)]
                max_val = max(max_val, X_START + len(classifiers_arr) + index)

            pos_y_cls = pos_y_cls + 5

        X_START = max_val + 1

        pos_y_cls = 0

        for index, score in enumerate(scores):
            print(index, score)
            new_labels[X_START + index] = score["name"]
            new_positions[X_START + index] = (150, pos_y_cls)
            new_edges += [(7, X_START + index)]

            for connection_name in score["from"]:
                new_edges += [(self.__find_element_by_name(connection_name, classifiers_arr)["index"], X_START + index)]

            pos_y_cls -= 10

        G = nx.DiGraph()

        edges = [
            (0, 1),
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 5),
            (3, 6),
            (4, 7),
        ]

        edges += new_edges
        edge_color = ["black" for i in range(len(edges))]
        pos = {
            0: (0, 20),
            1: (20, 20),
            2: (40, 20),
            3: (40, 10),
            4: (40, 0),
            5: (60, 20),
            6: (60, 10),
            7: (60, 0),
        }
        pos.update(new_positions)
        labels = {
            0: "dataset",
            1: "clean",
            2: "train",
            3: "validate",
            4: "test",
            5: "transformation",
            6: "transformation",
            7: "transformation",
        }
        labels.update(new_labels)

        nodes = np.arange(0, len(labels)).tolist()

        print(len(edges), len(edge_color))

        G.add_nodes_from(nodes)
        G.add_edges_from(edges)

        fig = plt.figure(1, figsize=(20, 6))
        nx.draw_networkx(G, pos=pos, labels=labels, arrows=True, node_shape="s", edge_color=edge_color,
                         bbox=dict(facecolor="skyblue", boxstyle="round", ec="silver", pad=0.3))
        # , connectionstyle="arc3,rad=0.05"

        plt.title("Analysis representation")
        plt.savefig("mindmap.png")
        # plt.show()

    def __find_element_by_name(self, name, classifiers_arr):
        for cls in classifiers_arr:
            if cls["name"] == name:
                return cls
        return None
