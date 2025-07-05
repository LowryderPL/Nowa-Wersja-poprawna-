import json
import os
from Core_achievement_tracker import AchievementTracker

RECIPES_FILE = "alchemy_recipes.json"
PLAYER_DATA_FILE = "player_data.json"

class AlchemySystem:
    def __init__(self):
        self.recipes = self.load_recipes()
        self.achievements = AchievementTracker()

    def load_recipes(self):
        if not os.path.exists(RECIPES_FILE):
            print("Brak pliku z przepisami alchemicznymi.")
            return []
        with open(RECIPES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def craft(self, ingredients):
        for recipe in self.recipes:
            if set(recipe["ingredients"]) == set(ingredients):
                result = recipe["result"]
                self._grant_xp(recipe)
                self.achievements.check_and_unlock("potion_crafted")
                print(f"Stworzono miksturę: {result}")
                return result
        print("Niepoprawna kombinacja składników.")
        return None

    def _grant_xp(self, recipe):
        xp_reward = recipe.get("xp", 5)
        if not os.path.exists(PLAYER_DATA_FILE):
            return
        with open(PLAYER_DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        current_xp = data.get("xp", 0)
        data["xp"] = current_xp + xp_reward
        with open(PLAYER_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    alchemy = AlchemySystem()
    test_mix = ["ziele krwi", "cień nocy"]
    alchemy.craft(test_mix)