import tkinter as tk
from tkinter import messagebox

FACTIONS = [
    {
        "name": "Zakon Welesa",
        "description": "Mroczna frakcja czarnoksiężników i rytualistów. Bonus: +10 XP na start.",
        "allowed_classes": ["Welesianin", "Kościejarz"],
        "bonus": {"xp": 10}
    },
    {
        "name": "Strażnicy Boru",
        "description": "Obrońcy lasów i dzikiej natury. Bonus: Startowy łuk myśliwski.",
        "allowed_classes": ["Borowiec", "Żmijogniew"],
        "bonus": {"item": {"name": "Łuk Borowca", "level": 1}}
    },
    {
        "name": "Córki Szeptu",
        "description": "Frakcja zielarek, uzdrowicielek i czarownic. Bonus: Mikstura uzdrowienia.",
        "allowed_classes": ["Szeptucha"],
        "bonus": {"item": {"name": "Mikstura Leczenia", "level": 1}}
    },
    {
        "name": "Toporni Synowie",
        "description": "Brutalna frakcja wojowników i egzekutorów. Bonus: +5 XP i hełm bojowy.",
        "allowed_classes": ["Topornik"],
        "bonus": {"xp": 5, "item": {"name": "Hełm Topornika", "level": 1}}
    }
]

class FactionGUI:
    def __init__(self, master, player_data):
        self.master = master
        self.master.title("Wybór Frakcji")
        self.master.geometry("720x520")
        self.player_data = player_data
        self.class_name = player_data.get("class", "Borowiec")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Wybierz frakcję dla swojej klasy:", font=("Times", 14)).pack(pady=10)
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        for faction in FACTIONS:
            if self.class_name in faction["allowed_classes"]:
                self.add_faction_card(faction)

    def add_faction_card(self, faction):
        card = tk.Frame(self.frame, bd=2, relief="ridge", padx=10, pady=10)
        card.pack(padx=10, pady=5, fill="x")

        tk.Label(card, text=faction["name"], font=("Georgia", 14, "bold")).pack(anchor="w")
        tk.Label(card, text=faction["description"], wraplength=600, justify="left").pack(anchor="w", pady=5)
        tk.Button(card, text="Wybierz", command=lambda f=faction: self.select_faction(f)).pack(anchor="e")

    def select_faction(self, faction):
        self.player_data["faction"] = faction["name"]
        xp_bonus = faction["bonus"].get("xp", 0)
        item_bonus = faction["bonus"].get("item")

        self.player_data["xp"] = self.player_data.get("xp", 0) + xp_bonus
        if item_bonus:
            if "inventory" not in self.player_data:
                self.player_data["inventory"] = []
            self.player_data["inventory"].append(item_bonus)

        messagebox.showinfo("Wybrano frakcję", f"Dołączono do: {faction['name']}!")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    player = {
        "class": "Welesianin",
        "class_rank": 0,
        "xp": 0,
        "inventory": []
    }
    app = FactionGUI(root, player)
    root.mainloop()