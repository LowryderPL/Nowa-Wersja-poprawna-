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

class InventoryGUI:
    def __init__(self, master, player_data):
        self.master = master
        self.master.title("Ekwipunek")
        self.master.geometry("700x500")
        self.player_data = player_data
        self.xp = player_data.get("xp", 0)
        self.items = player_data.get("inventory", [])
        self.class_name = player_data.get("class", "Żmijogniew")
        self.class_rank = player_data.get("class_rank", 0)

        self.create_widgets()

    def create_widgets(self):
        full_class = CLASSES.get(self.class_name, ["Nieznany"])[self.class_rank]
        tk.Label(self.master, text=f"Klasa: {full_class}", font=("Times", 14)).pack()
        tk.Label(self.master, text=f"XP: {self.xp}", font=("Times", 14)).pack()

        self.listbox = tk.Listbox(self.master, width=50, height=15)
        self.listbox.pack(pady=10)

        for item in self.items:
            lvl = item.get("level", 1)
            self.listbox.insert(tk.END, f"{item['name']} (Poziom {lvl})")

        tk.Button(self.master, text="Ulepsz przedmiot", command=self.upgrade_item).pack(pady=5)

    def upgrade_item(self):
        index = self.listbox.curselection()
        if not index:
            return

        item = self.items[index[0]]
        level = item.get("level", 1)
        cost = 10 * level

        if level >= 15:
            messagebox.showinfo("Maks", "Ten przedmiot ma już maksymalny poziom.")
            return

        if self.xp < cost:
            messagebox.showwarning("Brak XP", f"Potrzebujesz {cost} XP, aby ulepszyć.")
            return

        self.xp -= cost
        item["level"] = level + 1
        self.listbox.delete(index[0])
        self.listbox.insert(index[0], f"{item['name']} (Poziom {item['level']})")
        messagebox.showinfo("Ulepszono", f"{item['name']} → poziom {item['level']}")

if __name__ == "__main__":
    root = tk.Tk()
    player = {
        "xp": 100,
        "class": "Topornik",
        "class_rank": 1,
        "inventory": [
            {"name": "Topór Pęknięcia", "level": 3},
            {"name": "Hełm Runiczny", "level": 2}
        ]
    }
    app = InventoryGUI(root, player)
    root.mainloop()