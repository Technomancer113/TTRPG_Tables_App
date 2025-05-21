import random
from interfaces.loot_roller import LootRoller

class SimpleLootRoller(LootRoller):
    def roll_loot(self, table: list, rolls: int = 1) -> list:
        results = []
        for _ in range(rolls):
            if table:
                results.append(random.choice(table))
        return results
