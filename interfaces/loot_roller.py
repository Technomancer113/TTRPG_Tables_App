from abc import ABC, abstractmethod

class LootRoller(ABC):
    @abstractmethod
    def roll_loot(self, table: dict, rolls: int = 1) -> list:
        pass