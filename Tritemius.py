import tkinter as tk

class TritemiusCipher(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.color1 = '#072b63'
        self.color2 = '#bfe2ff'
        self.color3 = '#89b9e1'
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(
            self,
            bg=self.color1,
            fg=self.color2,
            font=('Arial', 22, 'bold'),
            text='Tritemius Cipher'
        )
        self.title.grid(column=0, row=0, sticky=tk.EW, pady=35)

        self.text_widget = tk.Text(
            self,
            bg=self.color2,
            fg=self.color1,
            selectbackground=self.color1,
            selectforeground=self.color2,
            font=('Arial', 17),
            height=5,
            padx=10,
            pady=10,
            highlightthickness=0,
            border=0
        )
        self.text_widget.grid(column=0, row=1, padx=100)

        self.button_encrypt = tk.Button(
            self,
            bg=self.color2,
            fg=self.color1,
            activebackground=self.color3,
            activeforeground=self.color1,
            font=('Arial', 15),
            text='Encrypt',
            width=6,
            height=1,
            cursor='hand1',
            highlightthickness=0,
            border=0,
            command=self.encrypt_text
        )
        self.button_encrypt.grid(column=0, row=2, pady=(38, 10))

        self.button_decrypt = tk.Button(
            self,
            bg=self.color2,
            fg=self.color1,
            activebackground=self.color3,
            activeforeground=self.color1,
            font=('Arial', 15),
            text='Decrypt',
            width=6,
            height=1,
            cursor='hand1',
            highlightthickness=0,
            border=0,
            command=self.decrypt_text
        )
        self.button_decrypt.grid(column=0, row=3)

    def encrypt_text(self):
        plaintext = self.text_widget.get("1.0", tk.END).upper()
        ciphertext = ''
        shift = 3  # Przykładowy przesunięcie dla szyfru Tritemiusza

        for char in plaintext:
            if char.isalpha():
                idx = (self.alphabet.index(char) + shift) % len(self.alphabet)
                ciphertext += self.alphabet[idx]
            else:
                ciphertext += char
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", ciphertext)

    def decrypt_text(self):
        ciphertext = self.text_widget.get("1.0", tk.END).upper()
        plaintext = ''
        shift = 3  # Przykładowy przesunięcie dla szyfru Tritemiusza

        for char in ciphertext:
            if char.isalpha():
                idx = (self.alphabet.index(char) - shift) % len(self.alphabet)
                plaintext += self.alphabet[idx]
            else:
                plaintext += char
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", plaintext)
