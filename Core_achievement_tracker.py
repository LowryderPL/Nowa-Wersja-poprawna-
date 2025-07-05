import json
import os

PLAYER_DATA_FILE = "player_data.json"

class Achievement:
    def __init__(self, name, description, condition_key):
        self.name = name
        self.description = description
        self.condition_key = condition_key

class AchievementTracker:
    def __init__(self):
        self.achievements = []
        self.unlocked = set()
        self.load_achievements()
        self.load_player_data()

    def load_achievements(self):
        self.achievements = [
            Achievement("First Blood", "Win your first arena battle", "arena_win_1"),
            Achievement("Herbalist", "Craft your first potion", "potion_crafted"),
            Achievement("Spellcaster", "Cast your first spell", "spell_casted"),
            Achievement("Explorer", "Complete your first quest", "quest_completed_1"),
            Achievement("Initiated", "Choose a class", "class_chosen")
        ]

    def load_player_data(self):
        if os.path.exists(PLAYER_DATA_FILE):
            with open(PLAYER_DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.unlocked = set(data.get("achievements", []))
        else:
            self.unlocked = set()

    def save_player_data(self):
        data = {}
        if os.path.exists(PLAYER_DATA_FILE):
            with open(PLAYER_DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)

        data["achievements"] = list(self.unlocked)

        with open(PLAYER_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def check_and_unlock(self, condition_key):
        for achievement in self.achievements:
            if achievement.condition_key == condition_key and achievement.name not in self.unlocked:
                self.unlocked.add(achievement.name)
                self.save_player_data()
                print(f"[OSIĄGNIĘCIE ODBLOKOWANE] {achievement.name}: {achievement.description}")

    def list_achievements(self):
        for a in self.achievements:
            status = "✔" if a.name in self.unlocked else "✘"
            print(f"{status} {a.name} - {a.description}")

if __name__ == "__main__":
    tracker = AchievementTracker()
    tracker.list_achievements()
    # tracker.check_and_unlock("quest_completed_1")  # przykład użycia