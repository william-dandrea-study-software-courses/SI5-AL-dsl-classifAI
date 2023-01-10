from domain.main.steps import HyperParameter


class C_HP(HyperParameter):

    def __init__(self, C: int):
        super().__init__()

        self.C: int = C
