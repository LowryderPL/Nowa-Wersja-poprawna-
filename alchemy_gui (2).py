import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from alchemy import AlchemySystem

class AlchemyGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Alchemia Firos")
        self.alchemy = AlchemySystem()
        self.selected_ingredients = []

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Wybierz składniki do mikstury:", font=("Times", 14)).pack(pady=10)

        self.ingredient_list = ["ziele krwi", "cień nocy", "korzeń życia", "pazur wilkołaka", "słona rosa"]
        self.ingredient_vars = {}

        for ingredient in self.ingredient_list:
            var = tk.IntVar()
            chk = tk.Checkbutton(self.master, text=ingredient, variable=var)
            chk.pack(anchor="w")
            self.ingredient_vars[ingredient] = var

        tk.Button(self.master, text="Stwórz miksturę", command=self.craft_potion).pack(pady=10)

        self.result_label = tk.Label(self.master, text="", font=("Times", 12), fg="green")
        self.result_label.pack()

    def craft_potion(self):
        self.selected_ingredients = [ing for ing, var in self.ingredient_vars.items() if var.get()]
        if len(self.selected_ingredients) != 2:
            messagebox.showwarning("Błąd", "Wybierz dokładnie 2 składniki!")
            return

        result = self.alchemy.craft(self.selected_ingredients)
        if result:
            self.result_label.config(text=f"Stworzono: {result}")
        else:
            self.result_label.config(text="Nie udało się stworzyć mikstury...")

if __name__ == "__main__":
    root = tk.Tk()
    gui = AlchemyGUI(root)
    root.mainloop()