from typing import List

from domain.main.steps.Step import Step
from utils.Cell import Cell


class Transformation(Step):

    def __init__(self):
        super().__init__()
        print("Preprocessing")

    def export(self) -> List[Cell]:
        pass
