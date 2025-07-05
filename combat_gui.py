import tkinter as tk
from tkinter import messagebox
import random
import json
import os

PLAYER_DATA_FILE = "player_data.json"

class CombatGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Walka z Przeciwnikiem")
        self.master.geometry("500x400")
        self.load_player_data()
        self.create_widgets()

    def load_player_data(self):
        if os.path.exists(PLAYER_DATA_FILE):
            with open(PLAYER_DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.xp = data.get("xp", 0)
            self.runes = data.get("runes", [])
        else:
            self.xp = 0
            self.runes = []

    def create_widgets(self):
        self.label_xp = tk.Label(self.master, text=f"XP Gracza: {self.xp}", font=("Arial", 14))
        self.label_xp.pack(pady=10)

        self.enemy_strength = random.randint(5, 15)
        self.label_enemy = tk.Label(self.master, text=f"Wróg pojawił się! Siła: {self.enemy_strength}", font=("Arial", 12))
        self.label_enemy.pack(pady=10)

        self.fight_button = tk.Button(self.master, text="Walcz", command=self.fight)
        self.fight_button.pack(pady=10)

        self.result_label = tk.Label(self.master, text="", font=("Arial", 12), fg="green")
        self.result_label.pack(pady=10)

    def fight(self):
        player_power = random.randint(4, 14)
        total_power = player_power + (3 if "Fizyczny" in self.runes else 0)

        if total_power >= self.enemy_strength:
            self.result_label.config(text=f"Pokonałeś wroga! (+10 XP)")
            self.xp += 10
            self.save_player_data()
            self.label_xp.config(text=f"XP Gracza: {self.xp}")
        else:
            self.result_label.config(text="Przeciwnik był silniejszy. Spróbuj ponownie.")
        self.fight_button.config(state=tk.DISABLED)

    def save_player_data(self):
        data = {"xp": self.xp, "runes": self.runes}
        with open(PLAYER_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = CombatGUI(root)
    root.mainloop()