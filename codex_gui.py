import tkinter as tk
from tkinter import ttk

CATEGORIES = {
    "Klasy": {
        "Żmijogniew": "Wojownik ognia i run, oparty na sile i rytuałach.",
        "Szeptucha": "Zielarka i uzdrowicielka, korzysta z mikstur i uroku.",
        "Welesianin": "Czarnoksiężnik krwi i śmierci. Rytuały i przeklęte zaklęcia.",
        "Borowiec": "Łowca, tropiciel, duch lasu. Władca zwierząt i łuku.",
        "Topornik": "Brutalna siła, pancerze i topory. Niszczy wszystko.",
        "Kościejarz": "Przyzywa zmarłych, manipuluje duszami. Władca umarłych.",
        "Wodnik Syn": "Zaklinacz lodu i wody. Mroźne zaklęcia i kontrola żywiołu."
    },
    "Frakcje": {
        "Zakon Welesa": "Mroczny kult rytualistów i krwi. Bonus: +10 XP.",
        "Strażnicy Boru": "Obrońcy przyrody. Startowy łuk i umiejętność tropienia.",
        "Córki Szeptu": "Zakon czarownic. Bonus: mikstura leczenia.",
        "Toporni Synowie": "Wojownicy i rębajły. Bonus: XP i hełm bojowy."
    },
    "Runy": {
        "Runa Ognia": "Zwiększa obrażenia zaklęć ognistych.",
        "Runa Krwi": "Wzmacnia rytuały Welesianina.",
        "Runa Wody": "Dodaje efekt zamrożenia zaklęciom lodu.",
        "Runa Cienia": "Zwiększa szansę uniku, działa z Krukiem Welesa."
    },
    "Potwory": {
        "Wilk Cienia": "Szybki, silny, zwinny. Spotykany w lasach północy.",
        "Upiorny Kruk": "Nadprzyrodzona istota zwiastująca śmierć.",
        "Nieumarły Strażnik": "Pilnuje katakumb. Odporny na mikstury.",
        "Leśna Ropucha": "Zmutowany potwór z bagien. Pluje toksyną."
    },
    "Lokacje": {
        "Zamek Kruka": "Twierdza starożytnego rodu. Centrum zakonu.",
        "Las Szeptów": "Miejsce mocy Szeptuch. Rośnie tam ziele lecznicze.",
        "Ruiny Welesa": "Zdewastowany ołtarz. Tu można rzucać rytuały.",
        "Katakumby Kości": "Pełne duchów, idealne dla Kościejarza."
    }
}

class CodexGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Kodeks Wiedzy FIROS")
        self.master.geometry("720x520")

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill="both")

        for category, entries in CATEGORIES.items():
            frame = tk.Frame(self.notebook)
            self.notebook.add(frame, text=category)

            listbox = tk.Listbox(frame, width=30)
            listbox.pack(side="left", fill="y", padx=5, pady=5)

            text = tk.Text(frame, wrap="word", font=("Times", 12))
            text.pack(side="right", expand=True, fill="both", padx=5, pady=5)

            for name in entries.keys():
                listbox.insert(tk.END, name)

            def show_info(event, entries=entries, listbox=listbox, text=text):
                selected = listbox.curselection()
                if selected:
                    name = listbox.get(selected[0])
                    text.delete("1.0", tk.END)
                    text.insert(tk.END, f"{name}\n\n{entries[name]}")

            listbox.bind("<<ListboxSelect>>", show_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = CodexGUI(root)
    root.mainloop()