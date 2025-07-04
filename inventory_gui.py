import tkinter as tk
from tkinter import messagebox
from xp_system import get_player_xp

class InventoryGUI:
    def __init__(self, master, player_data):
        self.master = master
        self.master.title("Ekwipunek")
        self.master.geometry("700x500")
        self.player_data = player_data
        self.xp = get_player_xp(player_data)
        self.items = player_data.get("inventory", [])

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text=f"XP: {self.xp}", font=("Times", 14)).pack()

        self.item_listbox = tk.Listbox(self.master, width=50, height=15, font=("Times", 12))
        self.item_listbox.pack(pady=10)

        for item in self.items:
            upgrade = item.get("level", 1)
            self.item_listbox.insert(tk.END, f"{item['name']} (poziom {upgrade})")

        tk.Button(self.master, text="Ulepsz przedmiot", command=self.upgrade_item, font=("Times", 12)).pack(pady=5)

    def upgrade_item(self):
        index = self.item_listbox.curselection()
        if not index:
            return

        item = self.items[index[0]]
        current_level = item.get("level", 1)

        if current_level >= 15:
            messagebox.showinfo("Maksymalny poziom", "Ten przedmiot osiągnął już maksymalny poziom.")
            return

        cost = 10 * current_level  # koszt ulepszenia zależny od poziomu
        if self.xp < cost:
            messagebox.showwarning("Za mało XP", f"Potrzebujesz {cost} XP, aby ulepszyć ten przedmiot.")
            return

        self.xp -= cost
        item["level"] = current_level + 1
        self.item_listbox.delete(index[0])
        self.item_listbox.insert(index[0], f"{item['name']} (poziom {item['level']})")
        messagebox.showinfo("Ulepszono", f"{item['name']} został ulepszony do poziomu {item['level']}.")

if __name__ == "__main__":
    root = tk.Tk()
    player = {
        "xp": 120,
        "inventory": [
            {"name": "Miecz Krwi", "level": 2},
            {"name": "Tarcza Cienia", "level": 1}
        ]
    }
    app = InventoryGUI(root, player)
    root.mainloop()