from domain.main.steps.Step import Step


class Preprocessing(Step):

    def __init__(self, url_dataset: str):
        super().__init__()
        self.url_dataset = url_dataset
