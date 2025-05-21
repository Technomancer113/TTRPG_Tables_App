from loot_engine.file_loot_table_store import FileLootTableStore
from loot_engine.openai_loot_generator import OpenAILootGenerator
from loot_engine.simple_loot_roller import SimpleLootRoller
from ui.cli_app import CLILootApp


def main():
    generator = OpenAILootGenerator()
    roller = SimpleLootRoller()
    store = FileLootTableStore()
    app = CLILootApp(generator, roller, store)
    app.run()


if __name__ == '__main__':
    main()
