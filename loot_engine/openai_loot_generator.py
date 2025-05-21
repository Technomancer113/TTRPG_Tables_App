import openai
import os
from interfaces.loot_generator import LootGenerator

class OpenAILootGenerator(LootGenerator):
    def generate_loot_table(self, context: str) -> dict:
        openai.api_key = os.getenv("OPENAI_API_KEY")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant who creates loot tables for tabletop RPGs. Return only a simple JSON list of loot item names."},
                {"role": "user", "content": f"Generate a loot table for: {context}"}
            ]
        )

        # Parse response (expects a list of strings)
        loot_items = response['choices'][0]['message']['content'].strip()
        return eval(loot_items) if loot_items.startswith("[") else []
