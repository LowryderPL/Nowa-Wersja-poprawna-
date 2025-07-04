import tkinter as tk

ACHIEVEMENTS = [
    {"name": "Pierwsza Krew", "description": "Pokonaj swojego pierwszego przeciwnika."},
    {"name": "Mistrz Craftingu", "description": "Utwórz 5 różnych przedmiotów."},
    {"name": "Zwierzolub", "description": "Zdobądź towarzysza."},
    {"name": "Badacz Kodeksu", "description": "Przeczytaj wpis w każdej zakładce kodeksu."},
    {"name": "Bogacz", "description": "Zdobądź 100 RFN."},
    {"name": "Runiczny Uczeń", "description": "Użyj runy w walce."},
    {"name": "Czempion Areny", "description": "Wygraj 10 pojedynków PvP."},
    {"name": "Odkrywca", "description": "Odwiedź 5 różnych lokacji na mapie."}
]

class AchievementsGUI:
    def __init__(self, master, player_data):
        self.master = master
        self.master.title("Osiągnięcia")
        self.master.geometry("600x500")
        self.player_data = player_data
        self.earned = player_data.get("achievements", [])

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Osiągnięcia Gracza", font=("Times", 16)).pack(pady=10)
        self.listbox = tk.Listbox(self.master, width=60, height=20)
        self.listbox.pack()

        for ach in ACHIEVEMENTS:
            name = ach["name"]
            mark = "✓" if name in self.earned else "✗"
            self.listbox.insert(tk.END, f"{mark} {name} — {ach['description']}")

if __name__ == "__main__":
    root = tk.Tk()
    player = {
        "achievements": ["Pierwsza Krew", "Zwierzolub", "Odkrywca"]
    }
    app = AchievementsGUI(root, player)
    root.mainloop()