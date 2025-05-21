from abc import ABC, abstractmethod

class LootTableStore(ABC):
    @abstractmethod
    def save_table(self, name: str, table: dict) -> None:
        pass

    @abstractmethod
    def load_table(self, name: str) -> dict:
        pass

    @abstractmethod
    def list_tables(self) -> list:
        pass
