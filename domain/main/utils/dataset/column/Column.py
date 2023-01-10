from abc import ABC, abstractmethod


class Column(ABC):

    def __init__(self):
        self.default_transformation = True
        self.name = ""

    def set_default_transformation(self, is_default: bool):
        self.default_transformation = is_default

    def set_name(self, name: str):
        self.name = name
