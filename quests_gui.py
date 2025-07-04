import tkinter as tk
from tkinter import messagebox

# Klasy i rangi FIROS
CLASSES = {
    "Żmijogniew": ["Żmijowy Wojownik", "Mistrz Żmijogniewu", "Pradawny Rytualista"],
    "Szeptucha": ["Młoda Szeptucha", "Zielarka Z Czarodrzewa", "Arcyszeptucha"],
    "Welesianin": ["Krwawy Uczeń", "Mistrz Przekleństw", "Syn Welesa"],
    "Borowiec": ["Tropiciel", "Myśliwy Cienia", "Duch Boru"],
    "Topornik": ["Toporny Wojownik", "Rębajło", "Burzyciel Światów"],
    "Kościejarz": ["Nekronauta", "Kościany Pasterz", "Arcynieumarły"],
    "Wodnik Syn": ["Lodowy Czeladnik", "Wodny Zaklinacz", "Syn Mrozu"]
}

# Przykładowe zadania z warunkami i nagrodami
QUESTS = [
    {
        "name": "Rytuał Krwi",
        "required_class": "Welesianin",
        "min_rank": 0,
        "reward_xp": 30,
        "description": "Odpraw rytuał na ciele wroga i zbierz jego krew."
    },
    {
        "name": "Polowanie na Wilki",
        "required_class": "Borowiec",
        "min_rank": 0,
        "reward_xp": 20,
        "description": "Zabij 3 wilki w lesie północnym."
    },
    {
        "name": "Uzdrowienie Wieśniaka",
        "required_class": "Szeptucha",
        "min_rank": 0,
        "reward_xp": 15,
        "description": "Stwórz miksturę uzdrawiającą i pomóż choremu."
    },
    {
        "name": "Próba Topornika",
        "required_class": "Topornik",
        "min_rank": 1,
        "reward_xp": 40,
        "description": "Pokonaj strażnika bramy jedynie toporem bojowym."
    },
    {
        "name": "Zew Umarłych",
        "required_class": "Kościejarz",
        "min_rank": 2,
        "reward_xp": 50,
        "description": "Przyzwij ducha przodków z katakumb i przetrwaj próbę."
    }
]

class QuestsGUI:
    def __init__(self, master, player_data):
        self.master = master
        self.master.title("Zadania")
        self.master.geometry("700x500")
        self.player_data = player_data
        self.xp = player_data.get("xp", 0)
        self.player_class = player_data.get("class", "Borowiec")
        self.class_rank = player_data.get("class_rank", 0)
        self.available_quests = self.filter_quests()

        self.create_widgets()

    def filter_quests(self):
        return [
            quest for quest in QUESTS
            if quest["required_class"] == self.player_class and quest["min_rank"] <= self.class_rank
        ]

    def create_widgets(self):
        full_class = CLASSES.get(self.player_class, ["Nieznany"])[self.class_rank]
        tk.Label(self.master, text=f"Klasa: {full_class} | XP: {self.xp}", font=("Times", 14)).pack()

        self.quest_listbox = tk.Listbox(self.master, width=50, height=15)
        self.quest_listbox.pack(pady=10)

        for quest in self.available_quests:
            self.quest_listbox.insert(tk.END, quest["name"])

        tk.Button(self.master, text="Pokaż szczegóły", command=self.show_details).pack(pady=5)
        tk.Button(self.master, text="Wykonaj zadanie", command=self.complete_quest).pack()

        self.details_label = tk.Label(self.master, text="", wraplength=600, font=("Times", 12), fg="gray")
        self.details_label.pack(pady=10)

    def show_details(self):
        index = self.quest_listbox.curselection()
        if not index:
            return
        quest = self.available_quests[index[0]]
        self.details_label.config(text=f"{quest['description']}\nNagroda: {quest['reward_xp']} XP")

    def complete_quest(self):
        index = self.quest_listbox.curselection()
        if not index:
            return
        quest = self.available_quests.pop(index[0])
        self.xp += quest["reward_xp"]
        self.player_data["xp"] = self.xp

        self.quest_listbox.delete(index[0])
        self.details_label.config(text="")
        messagebox.showinfo("Wykonano", f"Ukończono: {quest['name']}! +{quest['reward_xp']} XP")

if __name__ == "__main__":
    root = tk.Tk()
    player = {
        "xp": 25,
        "class": "Welesianin",
        "class_rank": 0
    }
    app = QuestsGUI(root, player)
    root.mainloop()