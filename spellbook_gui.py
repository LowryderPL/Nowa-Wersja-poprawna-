import tkinter as tk
from tkinter import messagebox
from runes_data import RUNES
from xp_system import get_player_xp
from spells_data import SPELLS


class SpellbookGUI:
    def __init__(self, master, player_data):
        self.master = master
        self.master.title("Księga Czarów")
        self.master.geometry("700x500")
        self.player_data = player_data
        self.xp = get_player_xp(player_data)
        self.runes = player_data.get("runes", [])

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text=f"XP: {self.xp}", font=("Times", 14)).pack()

        self.spell_listbox = tk.Listbox(self.master, width=50, height=15, font=("Times", 12))
        self.spell_listbox.pack(pady=10)

        for spell in SPELLS:
            self.spell_listbox.insert(tk.END, f"{spell['name']} (lvl {spell['level_required']})")

        tk.Button(self.master, text="Rzuć zaklęcie", command=self.cast_spell, font=("Times", 12)).pack(pady=5)

    def cast_spell(self):
        index = self.spell_listbox.curselection()
        if not index:
            return
        spell = SPELLS[index[0]]
        if self.xp < spell["level_required"]:
            messagebox.showwarning("Za mały poziom", "Nie masz wystarczającego poziomu, by rzucić ten czar.")
            return
        bonus = self.check_rune_bonus(spell)
        messagebox.showinfo("Czar rzucony", f"Rzuciłeś {spell['name']}! {bonus}")

    def check_rune_bonus(self, spell):
        for rune in RUNES:
            if rune["name"].lower() in spell["name"].lower() and rune["name"] in self.runes:
                return f"Bonus z runy: {rune['effect']}"
        return "Brak aktywnej runy."


if __name__ == "__main__":
    root = tk.Tk()
    player = {
        "xp": 10,
        "runes": ["Runa Ognia", "Runa Krwi"]
    }
    app = SpellbookGUI(root, player)
    root.mainloop()