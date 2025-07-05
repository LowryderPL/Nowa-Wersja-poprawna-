import tkinter as tk
from tkinter import messagebox
import random
import json
import os
from Core_achievement_tracker import AchievementTracker

PLAYER_DATA_FILE = "player_data.json"

class ArenaBattle:
    def __init__(self, master):
        self.master = master
        self.master.title("Arena Walki")
        self.achievements = AchievementTracker()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="ARENA", font=("Helvetica", 20, "bold")).pack(pady=10)

        self.enter_button = tk.Button(self.master, text="Wejdź na Arenę", command=self.start_battle)
        self.enter_button.pack(pady=5)

        self.result_label = tk.Label(self.master, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

    def start_battle(self):
        player_strength = random.randint(5, 15)
        enemy_strength = random.randint(3, 12)

        result = "WYGRANA!" if player_strength >= enemy_strength else "PRZEGRANA!"
        self.result_label.config(text=f"Ty: {player_strength} vs Wróg: {enemy_strength} → {result}")

        if result == "WYGRANA!":
            self.gain_xp(10)
            self.achievements.check_and_unlock("arena_win_1")
            messagebox.showinfo("Sukces", "Pokonałeś przeciwnika i zdobywasz 10 XP!")
        else:
            messagebox.showinfo("Porażka", "Tym razem się nie udało. Spróbuj ponownie!")

    def gain_xp(self, amount):
        data = {}
        if os.path.exists(PLAYER_DATA_FILE):
            with open(PLAYER_DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

        data["xp"] = data.get("xp", 0) + amount

        with open(PLAYER_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = ArenaBattle(root)
    root.mainloop()