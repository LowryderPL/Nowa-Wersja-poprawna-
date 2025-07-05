import tkinter as tk
from tkinter import messagebox
import json
import os

PLAYER_DATA_FILE = "player_data.json"

CLASSES = {
    "Żerca": ["Uczeń Żercy", "Kapłan Żywiołów", "Starzec Run"],
    "Szeptucha": ["Uczennica", "Znachorka", "Mistrzyni Uroków"],
    "Wiedźmin": ["Nowicjusz", "Szermierz", "Mistrz Szkoły Kota"],
    "Runicznik": ["Pisarczyk", "Zgłębiciel Run", "Mistyk Pieśni"],
    "Skalnik": ["Myśliwy", "Strażnik Boru", "Zabójca Potworów"],
    "Guślarz": ["Zaklinacz", "Nekromanta", "Pan Dymów"]
}

class ClassSelectorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Wybór Klasy")
        self.master.geometry("400x500")
        self.selected_class = tk.StringVar()
        self.selected_rank = tk.StringVar()
        self.player_data = self.load_player_data()

        self.create_widgets()

    def load_player_data(self):
        if os.path.exists(PLAYER_DATA_FILE):
            with open(PLAYER_DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_player_data(self):
        self.player_data["class"] = self.selected_class.get()
        self.player_data["rank"] = self.selected_rank.get()
        with open(PLAYER_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self.player_data, f, ensure_ascii=False, indent=2)

    def create_widgets(self):
        tk.Label(self.master, text="Wybierz swoją klasę:", font=("Arial", 14)).pack(pady=10)

        self.class_menu = tk.OptionMenu(self.master, self.selected_class, *CLASSES.keys(), command=self.update_ranks)
        self.class_menu.pack(pady=5)

        tk.Label(self.master, text="Wybierz rangę:", font=("Arial", 12)).pack(pady=10)
        self.rank_menu = tk.OptionMenu(self.master, self.selected_rank, "")
        self.rank_menu.pack(pady=5)

        tk.Button(self.master, text="Zapisz wybór", command=self.confirm_selection).pack(pady=20)

    def update_ranks(self, selected_class):
        menu = self.rank_menu["menu"]
        menu.delete(0, "end")
        for rank in CLASSES[selected_class]:
            menu.add_command(label=rank, command=lambda value=rank: self.selected_rank.set(value))
        self.selected_rank.set(CLASSES[selected_class][0])

    def confirm_selection(self):
        if not self.selected_class.get() or not self.selected_rank.get():
            messagebox.showwarning("Błąd", "Wybierz klasę i rangę!")
            return
        self.save_player_data()
        messagebox.showinfo("Zapisano", f"Wybrano klasę: {self.selected_class.get()} ({self.selected_rank.get()})")

if __name__ == "__main__":
    root = tk.Tk()
    app = ClassSelectorGUI(root)
    root.mainloop()