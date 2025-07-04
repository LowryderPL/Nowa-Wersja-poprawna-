import tkinter as tk

class JournalGUI:
    def __init__(self, master, player_data):
        self.master = master
        self.master.title("Dziennik Przygodnika")
        self.master.geometry("720x500")
        self.player_data = player_data
        self.entries = player_data.get("journal", [])

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Dziennik Twoich Zadań i Wydarzeń", font=("Times", 16)).pack(pady=10)

        self.listbox = tk.Listbox(self.master, width=80, height=20)
        self.listbox.pack(pady=5)

        for entry in self.entries:
            self.listbox.insert(tk.END, f"{entry['title']} — {entry['status']}")

        self.text = tk.Text(self.master, height=10, wrap="word", font=("Times", 12))
        self.text.pack(pady=10, fill="x")

        self.listbox.bind("<<ListboxSelect>>", self.show_entry)

    def show_entry(self, event):
        index = self.listbox.curselection()
        if not index:
            return
        entry = self.entries[index[0]]
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, f"{entry['title']}\n\n{entry['description']}\n\nStatus: {entry['status']}")

if __name__ == "__main__":
    root = tk.Tk()
    player = {
        "journal": [
            {"title": "Spotkanie z Welesianinem", "description": "Otrzymałeś zadanie od mrocznego maga w ruinach Welesa.", "status": "W toku"},
            {"title": "Tajemnicza Ropucha", "description": "Znalazłeś gadającego płaza w bagnie. Coś ukrywa...", "status": "Zakończone"}
        ]
    }
    app = JournalGUI(root, player)
    root.mainloop()