import tkinter as tk
import sys
from Caesar import CaesarCipher
from Polibiusz import PolibiuszCipher
from Homofonic import HomofonicCipher
from Tritemius import TritemiusCipher
from Playfair import PlayfairCipher
def main():
    root = tk.Tk()
    root.title('Polibiusz Cipher')
    root.geometry('800x450')
    root.resizable(width=False, height=False)

    polibiusz_app = PolibiuszCipher(root)
    polibiusz_app.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

    operating_system = sys.platform
    root = tk.Tk()
    caesar_cipher_app = CaesarCipher(root)
    root.title = 'Caesar Cipher'
    root.geometry('800x450')

    root.resizable(width=False, height=False)

    root = tk.Tk()
    root.title('Homofonic Cipher')
    root.geometry('800x450')
    root.resizable(width=False, height=False)

    homofonic_app = HomofonicCipher(root)
    homofonic_app.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

    root = tk.Tk()
    root.title('Tritemius Cipher')
    root.geometry('800x450')
    root.resizable(width=False, height=False)

    tritemius_app = TritemiusCipher(root)
    tritemius_app.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

    root = tk.Tk()
    root.title('Playfair Cipher')
    root.geometry('800x450')
    root.resizable(width=False, height=False)

    playfair_app = PlayfairCipher(root)
    playfair_app.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/