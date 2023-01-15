from typing import List

from domain.main.steps.Step import Step
from utils.Cell import Cell


class Mining(Step):

    def __init__(self):
        super().__init__()
        print("Mining")

    def export(self) -> List[Cell]:
        pass
