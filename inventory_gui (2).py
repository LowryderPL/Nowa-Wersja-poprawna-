import tkinter as tk
from tkinter import messagebox
import json
import os

PLAYER_DATA_FILE = "player_data.json"

class InventoryGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Ekwipunek Gracza")
        self.master.geometry("600x500")
        self.player_data = self.load_player_data()

        self.create_widgets()

    def load_player_data(self):
        if os.path.exists(PLAYER_DATA_FILE):
            with open(PLAYER_DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"xp": 0, "runes": [], "items": []}

    def save_player_data(self):
        with open(PLAYER_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self.player_data, f, ensure_ascii=False, indent=2)

    def create_widgets(self):
        tk.Label(self.master, text=f"XP: {self.player_data.get('xp', 0)}", font=("Arial", 14)).pack(pady=5)

        runes = self.player_data.get("runes", [])
        items = self.player_data.get("items", [])

        tk.Label(self.master, text="Runy:", font=("Arial", 12, "bold")).pack()
        self.rune_listbox = tk.Listbox(self.master, height=6, width=50)
        for rune in runes:
            self.rune_listbox.insert(tk.END, rune)
        self.rune_listbox.pack(pady=5)

        tk.Label(self.master, text="Przedmioty:", font=("Arial", 12, "bold")).pack()
        self.item_listbox = tk.Listbox(self.master, height=10, width=50)
        for item in items:
            self.item_listbox.insert(tk.END, item)
        self.item_listbox.pack(pady=5)

        tk.Button(self.master, text="Dodaj Przedmiot Testowy", command=self.add_item).pack(pady=5)
        tk.Button(self.master, text="Zapisz Zmiany", command=self.save_player_data).pack(pady=5)

    def add_item(self):
        new_item = "Miecz Cienia"
        self.player_data["items"].append(new_item)
        self.item_listbox.insert(tk.END, new_item)
        messagebox.showinfo("Dodano", f"Dodano przedmiot: {new_item}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryGUI(root)
    root.mainloop()