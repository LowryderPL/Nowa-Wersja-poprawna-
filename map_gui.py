import tkinter as tk
from tkinter import messagebox
from functools import partial
import os

# Klasy i rangi FIROS (dla weryfikacji dostępu)
CLASSES = {
    "Żmijogniew": ["Żmijowy Wojownik", "Mistrz Żmijogniewu", "Pradawny Rytualista"],
    "Szeptucha": ["Młoda Szeptucha", "Zielarka Z Czarodrzewa", "Arcyszeptucha"],
    "Welesianin": ["Krwawy Uczeń", "Mistrz Przekleństw", "Syn Welesa"],
    "Borowiec": ["Tropiciel", "Myśliwy Cienia", "Duch Boru"],
    "Topornik": ["Toporny Wojownik", "Rębajło", "Burzyciel Światów"],
    "Kościejarz": ["Nekronauta", "Kościany Pasterz", "Arcynieumarły"],
    "Wodnik Syn": ["Lodowy Czeladnik", "Wodny Zaklinacz", "Syn Mrozu"]
}

# Lokacje na mapie z wymaganiami klasowymi (opcjonalnie)
LOCATIONS = [
    {"name": "Zamek Kruka", "x": 80, "y": 120, "class_required": None},
    {"name": "Ruiny Welesa", "x": 300, "y": 200, "class_required": "Welesianin"},
    {"name": "Dolina Cieni", "x": 200, "y": 320, "class_required": None},
    {"name": "Katakumby Kości", "x": 500, "y": 150, "class_required": "Kościejarz"},
    {"name": "Las Szeptów", "x": 400, "y": 380, "class_required": "Szeptucha"}
]

class MapGUI:
    def __init__(self, master, player_data):
        self.master = master
        self.master.title("Mapa Świata FIROS")
        self.master.geometry("640x480")
        self.player_data = player_data
        self.player_class = player_data.get("class", "Borowiec")

        self.canvas = tk.Canvas(master, width=640, height=480)
        self.canvas.pack()

        try:
            from PIL import Image, ImageTk
            map_img = Image.open("firos_map_dark.png")
            map_img = map_img.resize((640, 480))
            self.bg = ImageTk.PhotoImage(map_img)
            self.canvas.create_image(0, 0, anchor="nw", image=self.bg)
        except:
            self.canvas.create_text(320, 240, text="(Mapa FIROS)
Brak obrazu tła", font=("Times", 20), fill="gray")

        self.place_locations()

    def place_locations(self):
        for loc in LOCATIONS:
            x, y = loc["x"], loc["y"]
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="red")
            self.canvas.create_text(x, y - 12, text=loc["name"], fill="white", font=("Helvetica", 9, "bold"))
            self.canvas.tag_bind(
                self.canvas.create_text(x, y + 8, text="●", fill="red"),
                "<Button-1>",
                partial(self.handle_location_click, loc=loc)
            )

    def handle_location_click(self, event, loc):
        required = loc.get("class_required")
        if required and required != self.player_class:
            messagebox.showwarning("Brak dostępu", f"Tylko klasa {required} może wejść do: {loc['name']}")
            return
        messagebox.showinfo("Lokacja", f"Wchodzisz do: {loc['name']} (dalsze akcje mogą być podpięte)")

if __name__ == "__main__":
    root = tk.Tk()
    player = {
        "class": "Welesianin",
        "class_rank": 1
    }
    app = MapGUI(root, player)
    root.mainloop()