from typing import List

from dsl.main.preprocessing.cleaning_methods import DslCleaningMethod
from dsl.main.preprocessing.cleaning_methods.DeleteLineDslCleaningMethod import DeleteLineDslCleaningMethod
from dsl.main.preprocessing.dataset.columns.BooleanDslColumn import BooleanDslColumn
from dsl.main.preprocessing.dataset.columns.DslColumn import DslColumn
from dsl.main.preprocessing.dataset.columns.qualitative.QualitativeNominalDslColumn import QualitativeNominalDslColumn
from dsl.main.preprocessing.dataset.columns.qualitative.QualitativeOrdinalDslColumn import QualitativeOrdinalDslColumn
from dsl.main.preprocessing.dataset.columns.quantitative.QuantitativeContinuousDslColumn import \
    QuantitativeContinuousDslColumn
from dsl.main.preprocessing.dataset.columns.quantitative.QuantitativeDiscreteDslColumn import \
    QuantitativeDiscreteDslColumn


class DslDataset:

    def __init__(self, path: str):
        self.__path: str = path
        self.__columns: List[DslColumn] = []

    def define_boolean_col(self, name: str, true_value: str, false_value: str, is_label: bool = False, cleaning_method: DslCleaningMethod  = DeleteLineDslCleaningMethod(), use_default_transformation: bool = True):
        self.__columns.append(BooleanDslColumn(name=name, true_value=true_value, false_value=false_value, cleaning_method=cleaning_method, use_default_transformation=use_default_transformation, is_label=is_label))

    def define_qualitative_nominal_col(self, name: str, values: List[str], use_default_transformation: bool = True):
        self.__columns.append(QualitativeNominalDslColumn(name=name, values=values, use_default_transformation=use_default_transformation))

    def define_qualitative_ordinal_col(self, name: str, values: List[str], use_default_transformation: bool = True):
        self.__columns.append(QualitativeOrdinalDslColumn(name=name, values=values, use_default_transformation=use_default_transformation))

    def define_quantitative_discrete_col(self, name: str, use_default_transformation: bool = True):
        self.__columns.append(QuantitativeDiscreteDslColumn(name=name, use_default_transformation=use_default_transformation))

    def define_quantitative_continuous_col(self, name: str, use_default_transformation: bool = True):
        self.__columns.append(QuantitativeContinuousDslColumn(name=name, use_default_transformation=use_default_transformation))

