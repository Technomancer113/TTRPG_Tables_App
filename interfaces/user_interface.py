from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def run(self):
        pass