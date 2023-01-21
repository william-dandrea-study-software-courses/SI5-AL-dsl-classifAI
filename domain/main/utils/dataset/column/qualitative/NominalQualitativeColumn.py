from domain.main.utils.dataset.column.Column import Column
from utils.dataset.column.qualitative.QualitativeColumn import QualitativeColumn


class NominalQualitativeColumn(QualitativeColumn):
    def __init__(self):
        super().__init__()

    def get_type(self) -> str:
        return "Nominal Qualitative"

    def export_transformation(self):

        code_cell = ""

        if self.get_default_transformation():
            code_cell += f'\tone_hot_encoder = OneHotEncoder( categories=[{self.get_possible_values()}])\n' \
                         f'\tX_train_encoded_values = one_hot_encoder.fit_transform(X_train[["{self.get_name()}"]]).toarray()\n' \
                         f'\tX_val_encoded_values = one_hot_encoder.fit_transform(X_val[["{self.get_name()}"]]).toarray()\n' \
                         f'\tX_test_encoded_values = one_hot_encoder.fit_transform(X_test[["{self.get_name()}"]]).toarray()\n' \
                         f'\t\n' \
                         f'\t\n' \
                         f'\tX_train_encoded = pd.DataFrame(X_train_encoded_values, columns=[f"{self.get_name()}_{{x}}" for x in one_hot_encoder.categories_[0]])\n' \
                         f'\tX_val_encoded = pd.DataFrame(X_val_encoded_values, columns=[f"{self.get_name()}_{{x}}" for x in one_hot_encoder.categories_[0]])\n' \
                         f'\tX_test_encoded = pd.DataFrame(X_test_encoded_values, columns=[f"{self.get_name()}_{{x}}" for x in one_hot_encoder.categories_[0]])\n' \
                         f'\tX_train = X_train.join(X_train_encoded)\n' \
                         f'\tX_val = X_val.join(X_val_encoded)\n' \
                         f'\tX_test = X_test.join(X_test_encoded)\n' \
                         f'\t\n' \
                         f'\tX_train = X_train.drop("{self.get_name()}", axis=1)\n' \
                         f'\tX_val = X_val.drop("{self.get_name()}", axis=1)\n' \
                         f'\tX_test = X_test.drop("{self.get_name()}", axis=1)\n'

        return code_cell
