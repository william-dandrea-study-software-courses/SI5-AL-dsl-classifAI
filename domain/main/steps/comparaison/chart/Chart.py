from abc import ABC, abstractmethod



class Chart(ABC):

    def __init__(self):
        super().__init__()
        print("Chart")
