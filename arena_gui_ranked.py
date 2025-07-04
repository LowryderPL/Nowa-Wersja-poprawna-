import tkinter as tk
from tkinter import messagebox
import random
from xp_system import get_player_xp

CLASSES = {
    "Żmijogniew": ["Żmijowy Wojownik", "Mistrz Żmijogniewu", "Pradawny Rytualista"],
    "Szeptucha": ["Młoda Szeptucha", "Zielarka Z Czarodrzewa", "Arcyszeptucha"],
    "Welesianin": ["Krwawy Uczeń", "Mistrz Przekleństw", "Syn Welesa"],
    "Borowiec": ["Tropiciel", "Myśliwy Cienia", "Duch Boru"],
    "Topornik": ["Toporny Wojownik", "Rębajło", "Burzyciel Światów"],
    "Kościejarz": ["Nekronauta", "Kościany Pasterz", "Arcynieumarły"],
    "Wodnik Syn": ["Lodowy Czeladnik", "Wodny Zaklinacz", "Syn Mrozu"]
}

class ArenaGUI:
    def __init__(self, master, player_data):
        self.master = master
        self.master.title("Arena PvP")
        self.master.geometry("720x500")
        self.player_data = player_data
        self.xp = get_player_xp(player_data)
        self.player_class = player_data.get("class", "Żmijogniew")
        self.class_rank = player_data.get("class_rank", 0)
        self.rank = player_data.get("rank", "Brąz")
        self.victories = player_data.get("victories", 0)

        self.create_widgets()

    def create_widgets(self):
        full_class_name = CLASSES[self.player_class][self.class_rank]
        tk.Label(self.master, text=f"Twoja klasa: {full_class_name}", font=("Times", 14)).pack()
        tk.Label(self.master, text=f"Twoje XP: {self.xp}", font=("Times", 14)).pack()
        tk.Label(self.master, text=f"Ranga PvP: {self.rank}", font=("Times", 14)).pack()
        tk.Label(self.master, text=f"Zwycięstwa: {self.victories}", font=("Times", 14)).pack()

        self.battle_button = tk.Button(self.master, text="Rozpocznij walkę", command=self.fight)
        self.battle_button.pack(pady=20)

        self.result_label = tk.Label(self.master, text="", font=("Times", 12))
        self.result_label.pack()

    def fight(self):
        enemy = self.generate_enemy()
        player_power = self.calculate_player_power()
        enemy_power = enemy["power"]

        result = ""
        if player_power >= enemy_power:
            self.victories += 1
            result = f"🛡️ Wygrałeś z {enemy['name']}!"
            self.xp += 20
            if self.victories >= 3:
                self.rank = self.promote_rank(self.rank)
                self.victories = 0
                if self.class_rank < 2:
                    self.class_rank += 1
        else:
            result = f"💀 Przegrałeś z {enemy['name']}..."
            self.xp = max(0, self.xp - 10)

        self.result_label.config(text=result)
        self.update_display()

    def calculate_player_power(self):
        base = self.xp
        bonus = 5 * (self.class_rank + 1)
        return base + bonus + random.randint(5, 15)

    def generate_enemy(self):
        names = ["Cień Kniei", "Upiór Zamieci", "Wilczy Topornik", "Skrwawiony Druid"]
        return {
            "name": random.choice(names),
            "power": random.randint(40, 90)
        }

    def promote_rank(self, current_rank):
        ranks = ["Brąz", "Srebro", "Złoto", "Platyna", "Diament"]
        if current_rank in ranks and ranks.index(current_rank) < len(ranks) - 1:
            return ranks[ranks.index(current_rank) + 1]
        return current_rank

    def update_display(self):
        self.master.destroy()
        root = tk.Tk()
        app = ArenaGUI(root, {
            "xp": self.xp,
            "class": self.player_class,
            "class_rank": self.class_rank,
            "rank": self.rank,
            "victories": self.victories
        })
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    player = {
        "xp": 60,
        "class": "Welesianin",
        "class_rank": 1,
        "rank": "Srebro",
        "victories": 2
    }
    app = ArenaGUI(root, player)
    root.mainloop()