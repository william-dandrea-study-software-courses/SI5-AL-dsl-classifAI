from dsl.main.preprocessing.cleaning_methods.DeleteLineDslCleaningMethod import DeleteLineDslCleaningMethod
from dsl.main.preprocessing.cleaning_methods.DslCleaningMethod import DslCleaningMethod
from dsl.main.preprocessing.cleaning_methods.ReplaceLineDslCleaningMethod import ReplaceLineDslCleaningMethod
from dsl.main.preprocessing.dataset.columns.DslColumn import DslColumn
from steps.preprocessing.cleaning.DeleteLineCleaningMethod import DeleteLineCleaningMethod
from steps.preprocessing.cleaning.ReplaceLineCleaningMethod import ReplaceLineCleaningMethod
from utils.dataset.column.Column import Column
from utils.dataset.column.quantitative.QuantitativeColumn import QuantitativeColumn


class QuantitativeDslColumn(DslColumn):

    def __init__(self, name: str, use_default_transformation: bool, cleaning_method: DslCleaningMethod):
        super().__init__(name, use_default_transformation, cleaning_method)

    def _export_quantitative_column(self) -> QuantitativeColumn:
        column: QuantitativeColumn = QuantitativeColumn()
        column.set_name(self._name)
        column.set_default_transformation(self._use_default_transformation)

        column.set_cleaning_method(self._cleaning_method.export())

        return column
