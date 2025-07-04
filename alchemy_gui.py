import tkinter as tk
from tkinter import messagebox

class AlchemyGUI:
    def __init__(self, master, player_data):
        self.master = master
        self.master.title("Alchemia")
        self.master.geometry("700x500")
        self.player_data = player_data
        self.ingredients = player_data.get("ingredients", {})
        self.potions = [
            {"name": "Mikstura Leczenia", "requires": {"ziele": 2, "woda": 1}, "effect": "Odzyskujesz zdrowie"},
            {"name": "Mikstura Mocy", "requires": {"ognik": 1, "krew potwora": 2}, "effect": "+10 do ataku"},
            {"name": "Zwój Ognia", "requires": {"popiół": 2, "runa ognia": 1}, "effect": "Rzucasz czar ognia"}
        ]

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Twoje składniki:", font=("Times", 14)).pack()

        self.ingredients_text = tk.Text(self.master, height=5, width=60)
        self.ingredients_text.pack()
        self.refresh_ingredients_display()

        tk.Label(self.master, text="Dostępne mikstury i zwoje:", font=("Times", 14)).pack(pady=5)

        self.potion_listbox = tk.Listbox(self.master, width=50, height=10)
        self.potion_listbox.pack()

        for potion in self.potions:
            self.potion_listbox.insert(tk.END, potion["name"])

        tk.Button(self.master, text="Stwórz miksturę / zwój", command=self.craft_potion).pack(pady=10)

    def refresh_ingredients_display(self):
        self.ingredients_text.delete("1.0", tk.END)
        for ing, qty in self.ingredients.items():
            self.ingredients_text.insert(tk.END, f"{ing}: {qty}\n")

    def craft_potion(self):
        index = self.potion_listbox.curselection()
        if not index:
            return
        potion = self.potions[index[0]]
        required = potion["requires"]

        for ing, qty in required.items():
            if self.ingredients.get(ing, 0) < qty:
                messagebox.showwarning("Brak składników", f"Nie masz wystarczająco: {ing}")
                return

        # Odejmujemy składniki
        for ing, qty in required.items():
            self.ingredients[ing] -= qty

        self.refresh_ingredients_display()
        messagebox.showinfo("Udało się!", f"Stworzyłeś: {potion['name']} – {potion['effect']}")

if __name__ == "__main__":
    root = tk.Tk()
    player = {
        "ingredients": {
            "ziele": 3,
            "woda": 2,
            "ognik": 1,
            "krew potwora": 3,
            "popiół": 2,
            "runa ognia": 1
        }
    }
    app = AlchemyGUI(root, player)
    root.mainloop()