from typing import List

from domain.main.utils.dataset.column.Column import Column


class Dataset:

    def __init__(self):
        self.columns: List[Column] = []
        self.use_default_transformation: bool = True

    def add_column(self, column: Column):
        self.columns.append(column)

    def change_use_default_transformation(self, use_default: bool):
        self.use_default_transformation = use_default
