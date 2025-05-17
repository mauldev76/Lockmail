import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import dialogs
from clipboard_utils import copy_text
from vigenere import *

def create_window(apps):
    extra_window = ttk.Toplevel()
    extra_window.title("LockMail")
    extra_window.geometry("600x500")
    apps(extra_window)

class Enkripsi(ttk.Frame):
    def __init__(self, master, title="Enkripsi", on_submit_callback=None):
        super().__init__(master, padding=30)
        self.pack(fill=BOTH, expand=YES)

        self.kunci = ttk.StringVar(value="")
        self.on_submit_callback = on_submit_callback or self.default_submit

        self.create_ui(title)

    def create_ui(self, title):
        ttk.Label(self, text=title, font=("Segoe UI", 30, "bold"), anchor=CENTER).pack(pady=(10, 20))

        card = ttk.Frame(self, padding=20, bootstyle="secondary")
        card.pack(fill=BOTH, expand=YES)

        self.create_form_entry(card, "Masukan Kunci:", self.kunci)

        ttk.Label(card, text="Masukan Judul dan Isi Email").pack(anchor=W, pady=(15, 5))
        self.textbox = ttk.Text(card, height=10, wrap="word")
        self.textbox.pack(fill=BOTH, expand=YES)

        self.create_buttonbox(card)

    def create_form_entry(self, parent, label, variable):
        container = ttk.Frame(parent)
        container.pack(fill=X, pady=5)

        ttk.Label(container, text=label, width=15).pack(side=LEFT)
        ttk.Entry(container, textvariable=variable).pack(side=LEFT, fill=X, expand=YES)

    def create_buttonbox(self, parent):
        box = ttk.Frame(parent)
        box.pack(fill=X, pady=(15, 0))

        ttk.Button(box, text="Submit", command=self.on_submit_callback, bootstyle=SUCCESS, width=10).pack(side=RIGHT, padx=5)
        ttk.Button(box, text="Cancel", command=self.on_cancel, bootstyle=SECONDARY, width=10).pack(side=RIGHT, padx=5)

    def default_submit(self):
        teks = self.textbox.get("1.0", "end").strip()
        kunci = self.kunci.get().strip()
        pesan = enkripsi_vigenere(teks, kunci)
        if dialogs.Messagebox.yesno(pesan, "Salin ke clipboard?"):
            copy_text(pesan)
            dialogs.Messagebox.show_info("Pesan telah disalin.")
        print("Enkripsi:", pesan)

    def on_cancel(self):
        self.winfo_toplevel().destroy()

class Dekripsi(Enkripsi):
    def __init__(self, master):
        super().__init__(master, title="Dekripsi", on_submit_callback=self.on_decrypt)

    def on_decrypt(self):
        teks = self.textbox.get("1.0", "end").strip()
        kunci = self.kunci.get().strip()
        pesan = dekripsi_vigenere(teks, kunci)
        if dialogs.Messagebox.yesno(pesan, "Salin ke clipboard?"):
            copy_text(pesan)
            dialogs.Messagebox.show_info("Pesan telah disalin.")
        print("Dekripsi:", pesan)


if __name__ == "__main__":
    app = ttk.Window("LockMail", "cyborg", resizable=(False, False))
    app.geometry("300x200")

    container = ttk.Frame(app, padding=20)
    container.pack(expand=YES)

    ttk.Label(container, text="LockMail", font=("Segoe UI", 28, "bold")).pack(pady=(10, 20))

    ttk.Button(container, text="🔐 Enkripsi", command=lambda: create_window(Enkripsi),
               bootstyle=SUCCESS, width=20).pack(pady=5)
    ttk.Button(container, text="🔓 Dekripsi", command=lambda: create_window(Dekripsi),
               bootstyle=PRIMARY, width=20).pack(pady=5)

    app.mainloop()