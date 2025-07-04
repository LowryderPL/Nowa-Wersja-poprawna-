import tkinter as tk
from tkinter import messagebox
from functools import partial
import subprocess
import sys
import os

# Główne dane gracza – do testów
player_data = {
    "xp": 50,
    "class": "Borowiec",
    "class_rank": 1,
    "rank": "Srebro",
    "victories": 2,
    "inventory": [
        {"name": "Łuk Borowca", "level": 2},
        {"name": "Peleryna Cienia", "level": 1}
    ]
}

# Funkcja do dynamicznego otwierania innych modułów (jeśli są w tym samym folderze)
def open_module(file_name, data):
    try:
        path = os.path.join(os.path.dirname(__file__), file_name)
        subprocess.run([sys.executable, path])
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie można otworzyć: {file_name}\n{str(e)}")

class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("FIROS: Magic & Magic")
        self.master.geometry("600x400")

        tk.Label(master, text="FIROS: Magic & Magic", font=("Georgia", 20, "bold")).pack(pady=20)
        tk.Label(master, text=f"Klasa: {player_data['class']} ({player_data['class_rank']}) | XP: {player_data['xp']}", font=("Times", 12)).pack()
        tk.Label(master, text=f"Ranga PvP: {player_data['rank']} | Zwycięstwa: {player_data['victories']}", font=("Times", 12)).pack(pady=5)

        tk.Button(master, text="📦 Ekwipunek", command=partial(open_module, "inventory_gui.py", player_data), width=30).pack(pady=5)
        tk.Button(master, text="🧪 Alchemia", command=partial(open_module, "alchemy_gui.py", player_data), width=30).pack(pady=5)
        tk.Button(master, text="📘 Księga Czarów", command=partial(open_module, "spellbook_gui.py", player_data), width=30).pack(pady=5)
        tk.Button(master, text="⚔️ Arena PvP", command=partial(open_module, "arena_gui_ranked.py", player_data), width=30).pack(pady=5)

        tk.Button(master, text="Wyjście", command=master.quit, fg="red").pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()