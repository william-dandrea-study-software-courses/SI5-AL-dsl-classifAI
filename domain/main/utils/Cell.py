from enum import Enum

import nbformat


class CellTypeEnum(Enum):
    CODE = 0,
    MARKDOWN = 1


class Cell:

    def __init__(self, content_in_cell: str, cell_type: CellTypeEnum):
        self.__content_in_cell = content_in_cell
        self.__cell_type = cell_type

    def export(self):
        if self.__cell_type == CellTypeEnum.CODE:
            return nbformat.v4.new_code_cell(self.__content_in_cell)

        return nbformat.v4.new_markdown_cell(self.__content_in_cell)
