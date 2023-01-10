import nbformat

from domain.main.steps.Step import Step
from utils.dataset.Dataset import Dataset


class Preprocessing(Step):

    def __init__(self, url_dataset: str, is_dataset_contains_headers_name: bool = False):
        super().__init__()
        self.url_dataset = url_dataset
        self.is_dataset_contains_headers_name = is_dataset_contains_headers_name
        self.dataset: Dataset = None

    def add_dataset(self, dataset: Dataset):
        self.dataset = dataset

    def generate(self):

        if self.dataset is None:
            raise Exception("A dataset is required for generate the Jupyter notebook file")

        description_content = f"# Préprocessing"
        description_cell = nbformat.v4.new_markdown_cell(description_content)

        load_description_content = f"## We import the dataset"
        load_description_cell = nbformat.v4.new_markdown_cell(load_description_content)

        cell_code = f'def load_dataset(dataset_url: str) -> pd.DataFrame: \n' \
                    f'    current_dataset = pd.read_csv(dataset_url, header={1 if self.is_dataset_contains_headers_name else None}) \n' \
                    f'    current_dataset.columns = {[col.name for col in self.dataset.columns]} \n' \
                    f'    return current_dataset \n' \
                    f'\n' \
                    f'load_dataset("{self.url_dataset}") \n' \
                    f''
        code_cell = nbformat.v4.new_code_cell(cell_code)

        return [description_cell, load_description_cell, code_cell]
