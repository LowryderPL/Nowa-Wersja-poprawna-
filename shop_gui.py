import tkinter as tk
from tkinter import messagebox

SHOP_ITEMS = [
    {"name": "Mikstura Leczenia", "price_rfn": 10, "price_ton": 0, "class_required": None},
    {"name": "Zwój Ognia", "price_rfn": 15, "price_ton": 0, "class_required": "Żmijogniew"},
    {"name": "Runa Krwi", "price_rfn": 0, "price_ton": 2, "class_required": "Welesianin"},
    {"name": "Hełm Topornika", "price_rfn": 20, "price_ton": 0, "class_required": "Topornik"},
    {"name": "Amulet Lasu", "price_rfn": 8, "price_ton": 0, "class_required": "Borowiec"},
    {"name": "Mikstura Cienia", "price_rfn": 0, "price_ton": 1, "class_required": "Szeptucha"}
]

class ShopGUI:
    def __init__(self, master, player_data):
        self.master = master
        self.master.title("Sklep FIROS")
        self.master.geometry("720x480")
        self.player_data = player_data
        self.class_name = player_data.get("class", "")
        self.rfn = player_data.get("rfn", 50)
        self.ton = player_data.get("ton", 1)
        self.inventory = player_data.get("inventory", [])

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text=f"RFN: {self.rfn} | TON: {self.ton}", font=("Times", 14)).pack(pady=5)
        tk.Label(self.master, text=f"Twoja klasa: {self.class_name}", font=("Times", 12)).pack()

        self.shop_listbox = tk.Listbox(self.master, width=50, height=15)
        self.shop_listbox.pack(pady=10)

        self.filtered_items = [item for item in SHOP_ITEMS if item["class_required"] in (None, self.class_name)]
        for item in self.filtered_items:
            price_info = f"{item['price_rfn']} RFN" if item['price_rfn'] > 0 else f"{item['price_ton']} TON"
            self.shop_listbox.insert(tk.END, f"{item['name']} — {price_info}")

        tk.Button(self.master, text="Kup", command=self.buy_item).pack(pady=5)

    def buy_item(self):
        index = self.shop_listbox.curselection()
        if not index:
            return

        item = self.filtered_items[index[0]]
        if item["price_rfn"] > 0:
            if self.rfn >= item["price_rfn"]:
                self.rfn -= item["price_rfn"]
                self.add_to_inventory(item)
                messagebox.showinfo("Zakup", f"Kupiłeś {item['name']} za {item['price_rfn']} RFN.")
            else:
                messagebox.showwarning("Brak RFN", "Nie masz wystarczającej ilości RFN.")
        elif item["price_ton"] > 0:
            if self.ton >= item["price_ton"]:
                self.ton -= item["price_ton"]
                self.add_to_inventory(item)
                messagebox.showinfo("Zakup", f"Kupiłeś {item['name']} za {item['price_ton']} TON.")
            else:
                messagebox.showwarning("Brak TON", "Nie masz wystarczającej ilości TON.")

        self.player_data["rfn"] = self.rfn
        self.player_data["ton"] = self.ton

    def add_to_inventory(self, item):
        self.inventory.append({"name": item["name"], "level": 1})
        self.player_data["inventory"] = self.inventory

if __name__ == "__main__":
    root = tk.Tk()
    player = {
        "class": "Welesianin",
        "rfn": 50,
        "ton": 2,
        "inventory": []
    }
    app = ShopGUI(root, player)
    root.mainloop()