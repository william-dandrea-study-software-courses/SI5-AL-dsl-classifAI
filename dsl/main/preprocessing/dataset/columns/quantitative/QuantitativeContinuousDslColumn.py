from dsl.main.preprocessing.dataset.columns.quantitative.QuantitativeDslColumn import QuantitativeDslColumn


class QuantitativeContinuousDslColumn(QuantitativeDslColumn):
    def __init__(self, name: str, use_default_transformation: bool):
        super().__init__(name, use_default_transformation)
