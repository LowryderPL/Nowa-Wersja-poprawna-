import tkinter as tk
from tkinter import messagebox

CLASSES = {
    "Żmijogniew": ["Żmijowy Wojownik", "Mistrz Żmijogniewu", "Pradawny Rytualista"],
    "Szeptucha": ["Młoda Szeptucha", "Zielarka Z Czarodrzewa", "Arcyszeptucha"],
    "Welesianin": ["Krwawy Uczeń", "Mistrz Przekleństw", "Syn Welesa"],
    "Borowiec": ["Tropiciel", "Myśliwy Cienia", "Duch Boru"],
    "Topornik": ["Toporny Wojownik", "Rębajło", "Burzyciel Światów"],
    "Kościejarz": ["Nekronauta", "Kościany Pasterz", "Arcynieumarły"],
    "Wodnik Syn": ["Lodowy Czeladnik", "Wodny Zaklinacz", "Syn Mrozu"]
}

SPELLS = [
    {"name": "Rytuał Cienia", "required_class": "Welesianin", "rank": 1, "level_required": 30, "effect": "Zadaje 25 obrażeń"},
    {"name": "Lodowy Dotyk", "required_class": "Wodnik Syn", "rank": 0, "level_required": 10, "effect": "Spowalnia wroga"},
    {"name": "Urok Leczenia", "required_class": "Szeptucha", "rank": 0, "level_required": 5, "effect": "Przywraca 20 HP"},
    {"name": "Zew Kości", "required_class": "Kościejarz", "rank": 2, "level_required": 40, "effect": "Przywołuje sługę zmarłych"},
    {"name": "Wściekłość Kniei", "required_class": "Borowiec", "rank": 1, "level_required": 20, "effect": "+10 ataku na 3 tury"},
    {"name": "Runiczny Szał", "required_class": "Topornik", "rank": 2, "level_required": 35, "effect": "Podwaja atak przez 1 turę"}
]

class SpellbookGUI:
    def __init__(self, master, player_data):
        self.master = master
        self.master.title("Księga Czarów")
        self.master.geometry("720x500")
        self.player_data = player_data
        self.xp = player_data.get("xp", 0)
        self.player_class = player_data.get("class", "Szeptucha")
        self.class_rank = player_data.get("class_rank", 0)

        self.create_widgets()

    def create_widgets(self):
        full_class = CLASSES.get(self.player_class, ["Nieznany"])[self.class_rank]
        tk.Label(self.master, text=f"Klasa: {full_class} | XP: {self.xp}", font=("Times", 14)).pack()

        self.spell_listbox = tk.Listbox(self.master, width=50, height=15)
        self.spell_listbox.pack(pady=10)

        self.available_spells = [
            spell for spell in SPELLS
            if spell["required_class"] == self.player_class and spell["rank"] <= self.class_rank
        ]

        for spell in self.available_spells:
            self.spell_listbox.insert(tk.END, f"{spell['name']} (min XP: {spell['level_required']})")

        tk.Button(self.master, text="Rzuć zaklęcie", command=self.cast_spell).pack()

    def cast_spell(self):
        index = self.spell_listbox.curselection()
        if not index:
            return
        spell = self.available_spells[index[0]]
        if self.xp < spell["level_required"]:
            messagebox.showwarning("Za mało XP", f"Potrzeba {spell['level_required']} XP!")
            return
        messagebox.showinfo("Czar rzucony", f"{spell['name']} → {spell['effect']}")

if __name__ == "__main__":
    root = tk.Tk()
    player = {
        "xp": 36,
        "class": "Welesianin",
        "class_rank": 1
    }
    app = SpellbookGUI(root, player)
    root.mainloop()