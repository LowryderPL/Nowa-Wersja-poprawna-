import tkinter as tk
from tkinter import messagebox
import json
import os

PLAYER_DATA_FILE = "player_data.json"

SPELLS = [
    {"name": "Płomień Żercy", "level_required": 5, "element": "Ogień"},
    {"name": "Urok Szeptuchy", "level_required": 3, "element": "Umysł"},
    {"name": "Zamach Wiedźmina", "level_required": 6, "element": "Fizyczny"},
    {"name": "Runiczna Tarcza", "level_required": 4, "element": "Magia"},
    {"name": "Strzała Skalnika", "level_required": 2, "element": "Ziemia"},
    {"name": "Trupi Szept Guślarza", "level_required": 7, "element": "Cień"}
]

RUNES = {
    "Ogień": "Runiczna moc ognia zwiększa obrażenia.",
    "Umysł": "Runy umysłu zwiększają skuteczność uroków.",
    "Fizyczny": "Runy siły zwiększają szansę trafienia krytycznego.",
    "Magia": "Runy magii zwiększają czas działania czaru.",
    "Ziemia": "Runy ziemi zwiększają celność i obronę.",
    "Cień": "Runy cienia dają szansę na natychmiastowe pokonanie przeciwnika."
}

class SpellbookGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Księga Czarów")
        self.master.geometry("600x500")
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
        tk.Label(self.master, text=f"Twoje XP: {self.xp}", font=("Arial", 14)).pack(pady=10)

        self.spell_listbox = tk.Listbox(self.master, width=50, height=15)
        for spell in SPELLS:
            self.spell_listbox.insert(tk.END, f"{spell['name']} (lvl {spell['level_required']})")
        self.spell_listbox.pack(pady=10)

        tk.Button(self.master, text="Rzuć Zaklęcie", command=self.cast_spell).pack()

        self.status_label = tk.Label(self.master, text="", font=("Arial", 12), fg="green")
        self.status_label.pack(pady=10)

    def cast_spell(self):
        selection = self.spell_listbox.curselection()
        if not selection:
            return

        spell = SPELLS[selection[0]]
        if self.xp < spell["level_required"]:
            messagebox.showwarning("Zbyt niski poziom", "Nie masz wystarczającego poziomu XP.")
            return

        bonus = self.check_rune_bonus(spell)
        self.status_label.config(text=f"Rzucasz: {spell['name']} — {bonus}")

    def check_rune_bonus(self, spell):
        element = spell.get("element")
        if element in self.runes:
            return RUNES[element]
        return "Brak aktywnej runy."

if __name__ == "__main__":
    root = tk.Tk()
    app = SpellbookGUI(root)
    root.mainloop()