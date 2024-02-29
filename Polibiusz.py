import tkinter as tk

class PolibiuszCipher(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.color1 = '#072b63'
        self.color2 = '#bfe2ff'
        self.color3 = '#89b9e1'
        self.alphabet = {'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
                         'F': '21', 'G': '22', 'H': '23', 'I': '24', 'K': '25',
                         'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35',
                         'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45',
                         'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'}

        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(
            self,
            bg=self.color1,
            fg=self.color2,
            font=('Arial', 22, 'bold'),
            text='Polibiusz Cipher'
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
        for char in plaintext:
            if char == ' ':
                ciphertext += ' '
            else:
                ciphertext += self.alphabet.get(char, char) + ' '
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", ciphertext)

    def decrypt_text(self):
        ciphertext = self.text_widget.get("1.0", tk.END).strip()
        plaintext = ''
        i = 0
        while i < len(ciphertext):
            if ciphertext[i] == ' ':
                plaintext += ' '
            else:
                code = ciphertext[i:i+2]
                for char, value in self.alphabet.items():
                    if value == code:
                        plaintext += char
                        break
                i += 1
            i += 1
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", plaintext)

