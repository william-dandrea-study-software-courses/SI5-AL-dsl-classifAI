from typing import List

from domain.main.utils.dataset.column.Column import Column


class Dataset:

    def __init__(self):
        self.columns: List[Column] = []

    def add_column(self, column: Column):
        self.columns.append(column)
