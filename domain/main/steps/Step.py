from abc import ABC, abstractmethod


class Step(ABC):

    def __init__(self):
        print("Step")
