import tkinter as tk
from tkinter import messagebox

RECIPES = [
    {
        "name": "Miecz Żmijogniewu",
        "class_required": "Żmijogniew",
        "ingredients": ["Stal", "Runa Ognia"],
        "result": {"name": "Miecz Żmijogniewu", "level": 1}
    },
    {
        "name": "Zbroja Borowca",
        "class_required": "Borowiec",
        "ingredients": ["Skóra Wilka", "Kora Dębu"],
        "result": {"name": "Zbroja Borowca", "level": 1}
    },
    {
        "name": "Zwój Leczenia",
        "class_required": "Szeptucha",
        "ingredients": ["Ziele Lecznicze", "Papirus"],
        "result": {"name": "Zwój Leczenia", "level": 1}
    }
]

class CraftingGUI:
    def __init__(self, master, player_data):
        self.master = master
        self.master.title("Rzemiosło i Artefakty")
        self.master.geometry("700x500")
        self.player_data = player_data
        self.player_class = player_data.get("class", "")
        self.inventory = player_data.get("inventory", [])
        self.selected_recipe = None

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text=f"Klasa: {self.player_class}", font=("Times", 14)).pack(pady=5)
        self.recipe_listbox = tk.Listbox(self.master, width=40, height=10)
        self.recipe_listbox.pack(pady=10)

        self.available_recipes = [r for r in RECIPES if r["class_required"] == self.player_class]
        for recipe in self.available_recipes:
            self.recipe_listbox.insert(tk.END, recipe["name"])

        tk.Button(self.master, text="Pokaż przepis", command=self.show_recipe).pack()
        self.ingredients_label = tk.Label(self.master, text="", font=("Times", 12))
        self.ingredients_label.pack(pady=5)
        tk.Button(self.master, text="Wytwórz", command=self.craft_item).pack(pady=10)

        self.status_label = tk.Label(self.master, text="", fg="green", font=("Times", 12))
        self.status_label.pack(pady=5)

    def show_recipe(self):
        index = self.recipe_listbox.curselection()
        if not index:
            return
        self.selected_recipe = self.available_recipes[index[0]]
        ingredients = self.selected_recipe["ingredients"]
        self.ingredients_label.config(text=f"Wymagane składniki: {', '.join(ingredients)}")

    def craft_item(self):
        if not self.selected_recipe:
            return
        ingredients = self.selected_recipe["ingredients"]
        inventory_names = [item["name"] for item in self.inventory]

        if all(ing in inventory_names for ing in ingredients):
            for ing in ingredients:
                for item in self.inventory:
                    if item["name"] == ing:
                        self.inventory.remove(item)
                        break
            new_item = self.selected_recipe["result"]
            self.inventory.append(new_item)
            self.status_label.config(text=f"Stworzono: {new_item['name']}")
        else:
            messagebox.showwarning("Brak składników", "Nie masz wszystkich wymaganych składników!")

if __name__ == "__main__":
    root = tk.Tk()
    player = {
        "class": "Szeptucha",
        "inventory": [
            {"name": "Ziele Lecznicze", "level": 1},
            {"name": "Papirus", "level": 1}
        ]
    }
    app = CraftingGUI(root, player)
    root.mainloop()