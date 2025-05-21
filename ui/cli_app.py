from interfaces.user_interface import UserInterface

class CLILootApp(UserInterface):
    def __init__(self, generator, roller, store):
        self.generator = generator
        self.roller = roller
        self.store = store

    def run(self):
        while True:
            print("\n[1] Generate Loot Table\n[2] Roll on Existing Table\n[3] List Tables\n[4] Quit")
            choice = input("> ")

            if choice == '1':
                context = input("Describe the loot context: ")
                table = self.generator.generate_loot_table(context)
                name = input("Save table as: ")
                self.store.save_table(name, table)
                print("Table saved.")

            elif choice == '2':
                name = input("Enter table name: ")
                rolls = int(input("How many rolls? "))
                table = self.store.load_table(name)
                results = self.roller.roll_loot(table, rolls)
                print("Loot Results:", results)

            elif choice == '3':
                print("Available Tables:", self.store.list_tables())

            elif choice == '4':
                break

            else:
                print("Invalid option.")