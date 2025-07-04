import tkinter as tk
from tkinter import messagebox

# Lista dostępnych zwierzaków
PETS = [
    {
        "name": "Wilk Cienia",
        "bonus": "Atak +5",
        "evolution": ["Wilk Cienia", "Czarny Wilk", "Wilczy Alf"],
        "class_required": "Borowiec"
    },
    {
        "name": "Ropucha Szeptuchy",
        "bonus": "Szansa na ogłuszenie",
        "evolution": ["Ropucha", "Ropucha Runiczna", "Królowa Ropuch"],
        "class_required": "Szeptucha"
    },
    {
        "name": "Kruk Welesa",
        "bonus": "Unik +5%",
        "evolution": ["Kruk", "Kruk Cieni", "Upiorny Kruk"],
        "class_required": "Welesianin"
    }
]

class PetGUI:
    def __init__(self, master, player_data):
        self.master = master
        self.master.title("Towarzysz / Pet")
        self.master.geometry("700x480")
        self.player_data = player_data
        self.player_class = player_data.get("class", "Borowiec")
        self.pet = player_data.get("pet", None)
        self.available_pets = [p for p in PETS if p["class_required"] == self.player_class]

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text=f"Twoja klasa: {self.player_class}", font=("Times", 14)).pack(pady=5)

        self.pet_listbox = tk.Listbox(self.master, width=40, height=10)
        self.pet_listbox.pack(pady=10)

        for pet in self.available_pets:
            self.pet_listbox.insert(tk.END, pet["name"])

        tk.Button(self.master, text="Zobacz szczegóły", command=self.show_pet_details).pack(pady=5)
        tk.Button(self.master, text="Aktywuj Peta", command=self.set_active_pet).pack(pady=5)
        self.details_label = tk.Label(self.master, text="", wraplength=600, font=("Times", 12), fg="gray")
        self.details_label.pack(pady=10)

    def show_pet_details(self):
        index = self.pet_listbox.curselection()
        if not index:
            return
        pet = self.available_pets[index[0]]
        evo = " ➝ ".join(pet["evolution"])
        self.details_label.config(text=f"{pet['name']} — Bonus: {pet['bonus']}\nEwolucje: {evo}")

    def set_active_pet(self):
        index = self.pet_listbox.curselection()
        if not index:
            return
        selected_pet = self.available_pets[index[0]]
        self.player_data["pet"] = {
            "name": selected_pet["name"],
            "level": 1,
            "bonus": selected_pet["bonus"]
        }
        messagebox.showinfo("Aktywowano", f"{selected_pet['name']} został Twoim towarzyszem!")

if __name__ == "__main__":
    root = tk.Tk()
    player = {
        "class": "Welesianin",
        "pet": None
    }
    app = PetGUI(root, player)
    root.mainloop()