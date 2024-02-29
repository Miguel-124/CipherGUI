import tkinter as tk
import sys
from Caesar import CaesarCipher
from Polibiusz import PolibiuszCipher
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/