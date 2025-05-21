import json
import os
from interfaces.loot_table_store import LootTableStore

class FileLootTableStore(LootTableStore):
    def __init__(self, directory='loot_tables'):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)

    def _path(self, name):
        return os.path.join(self.directory, f"{name}.json")

    def save_table(self, name, table):
        with open(self._path(name), 'w') as f:
            json.dump(table, f, indent=2)

    def load_table(self, name):
        with open(self._path(name), 'r') as f:
            return json.load(f)

    def list_tables(self):
        return [f[:-5] for f in os.listdir(self.directory) if f.endswith('.json')]

