import tkinter as tk
from Caesar import CaesarCipher
from Polibiusz import PolibiuszCipher
from Homofonic import HomofonicCipher
from Tritemius import TritemiusCipher
from Playfair import PlayfairCipher

class CipherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cipher Selection")
        self.geometry("600x100")

        # Create buttons for selecting ciphers
        self.caesar_button = tk.Button(self, text="Caesar Cipher", command=self.open_caesar)
        self.caesar_button.pack(side=tk.LEFT, padx=10)

        self.homofonic_button = tk.Button(self, text="Homofonic Cipher", command=self.open_homofonic)
        self.homofonic_button.pack(side=tk.LEFT, padx=10)

        self.polibiusz_button = tk.Button(self, text="Polibiusz Cipher", command=self.open_polibiusz)
        self.polibiusz_button.pack(side=tk.LEFT, padx=10)

        self.tritemius_button = tk.Button(self, text="Tritemius Cipher", command=self.open_tritemius)
        self.tritemius_button.pack(side=tk.LEFT, padx=10)

        self.playfair_button = tk.Button(self, text="Playfair Cipher", command=self.open_playfair)
        self.playfair_button.pack(side=tk.LEFT, padx=10)

    def open_caesar(self):
        self.destroy()
        root = tk.Tk()
        root.title('Caesar Cipher')
        root.geometry('800x450')
        root.resizable(width=False, height=False)
        cipher_app = CaesarCipher(root)
        root.mainloop()

    def open_homofonic(self):
        self.destroy()
        root = tk.Tk()
        root.title('Homofonic Cipher')
        root.geometry('800x450')
        root.resizable(width=False, height=False)
        homofonic_app = HomofonicCipher(root)
        homofonic_app.pack(fill=tk.BOTH, expand=True)
        root.mainloop()

    def open_polibiusz(self):
        self.destroy()
        root = tk.Tk()
        root.title('Polibiusz Cipher')
        root.geometry('800x450')
        root.resizable(width=False, height=False)
        polibiusz_app = PolibiuszCipher(root)
        polibiusz_app.pack(fill=tk.BOTH, expand=True)
        root.mainloop()

    def open_tritemius(self):
        self.destroy()
        root = tk.Tk()
        root.title('Tritemius Cipher')
        root.geometry('800x450')
        root.resizable(width=False, height=False)
        tritemius_app = TritemiusCipher(root)
        tritemius_app.pack(fill=tk.BOTH, expand=True)
        root.mainloop()

    def open_playfair(self):
        self.destroy()
        root = tk.Tk()
        root.title('Playfair Cipher')
        root.geometry('800x450')
        root.resizable(width=False, height=False)
        playfair_app = PlayfairCipher(root)
        playfair_app.pack(fill=tk.BOTH, expand=True)
        root.mainloop()

if __name__ == "__main__":
    app = CipherApp()
    app.mainloop()
