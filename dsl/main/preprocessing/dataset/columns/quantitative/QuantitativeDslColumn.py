from dsl.main.preprocessing.dataset.columns.DslColumn import DslColumn


class QuantitativeDslColumn(DslColumn):

    def __init__(self, name: str, use_default_transformation: bool):
        super().__init__(name, use_default_transformation)
