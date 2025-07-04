
import tkinter as tk
from tkinter import messagebox

# Nowe klasy postaci i ich rangi
CLASSES = {
    "Żmijogniew": ["Uczeń", "Mistrz", "Pradawny"],
    "Szeptucha": ["Nowicjuszka", "Wiedźma", "Starszyzna"],
    "Welesianin": ["Sługa", "Szaman", "Awatar"],
    "Borowiec": ["Myśliwy", "Strażnik", "Władca Kniei"],
    "Topornik": ["Zbrojny", "Rębajło", "Zwiastun Śmierci"],
    "Kościejarz": ["Skryba", "Kostuch", "Nekromanta"],
    "Wodnik Syn": ["Wodniak", "Fala", "Władca Głębin"]
}

RECIPES = {
    "Eliksir Welesianina": {"ingredients": ["Toadstool", "Mandrake", "Mushroom"], "effect": "Odnawia 10 many"},
    "Mikstura Borowca": {"ingredients": ["Puffball", "Bloodgrass"], "effect": "Dodaje +5 do ataku"},
    "Wywar Żmijogniewu": {"ingredients": ["Ranugrass", "Morrell"], "effect": "Zadaje 20 obrażeń przeciwnikowi"}
}

class AlchemyGUI:
    def __init__(self, master, player_class, player_rank):
        self.master = master
        self.master.title("System Alchemii")
        self.player_class = player_class
        self.player_rank = player_rank
        self.selected_ingredients = []
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text=f"Klasa: {self.player_class} ({self.player_rank})", font=("Times", 14)).pack()

        self.ingredients_listbox = tk.Listbox(self.master, selectmode=tk.MULTIPLE, width=40)
        self.ingredients_listbox.pack(pady=10)

        all_ingredients = set()
        for recipe in RECIPES.values():
            all_ingredients.update(recipe["ingredients"])
        for ing in sorted(all_ingredients):
            self.ingredients_listbox.insert(tk.END, ing)

        tk.Button(self.master, text="Ugotuj miksturę", command=self.brew).pack()

    def brew(self):
        selected = [self.ingredients_listbox.get(i) for i in self.ingredients_listbox.curselection()]
        for name, data in RECIPES.items():
            if set(data["ingredients"]) == set(selected):
                messagebox.showinfo("Mikstura", f"{name} stworzona! Efekt: {data['effect']}")
                return
        messagebox.showwarning("Niepowodzenie", "Nie znaleziono odpowiedniego przepisu.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AlchemyGUI(root, "Welesianin", "Szaman")
    root.mainloop()
