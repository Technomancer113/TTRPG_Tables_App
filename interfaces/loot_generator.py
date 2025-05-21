from abc import ABC, abstractmethod

class LootGenerator(ABC):
    @abstractmethod
    def generate_loot_table(self, context: str) -> dict:
        pass