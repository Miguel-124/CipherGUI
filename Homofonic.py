import tkinter as tk

class HomofonicCipher(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.color1 = '#072b63'
        self.color2 = '#bfe2ff'
        self.color3 = '#89b9e1'
        self.key = {'A': ['11', '12'], 'B': ['21', '22'], 'C': ['31', '32'], 'D': ['41', '42'],
                    'E': ['51', '52'], 'F': ['61', '62'], 'G': ['71', '72'], 'H': ['81', '82'],
                    'I': ['91', '92'], 'J': ['101', '102'], 'K': ['111', '112'], 'L': ['121', '122'],
                    'M': ['131', '132'], 'N': ['141', '142'], 'O': ['151', '152'], 'P': ['161', '162'],
                    'Q': ['171', '172'], 'R': ['181', '182'], 'S': ['191', '192'], 'T': ['201', '202'],
                    'U': ['211', '212'], 'V': ['221', '222'], 'W': ['231', '232'], 'X': ['241', '242'],
                    'Y': ['251', '252'], 'Z': ['261', '262']}

        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(
            self,
            bg=self.color1,
            fg=self.color2,
            font=('Arial', 22, 'bold'),
            text='Homofonic Cipher'
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
                codes = self.key.get(char, [])
                if codes:
                    ciphertext += codes[0] + ' '
                else:
                    ciphertext += char
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", ciphertext)

    def decrypt_text(self):
        ciphertext = self.text_widget.get("1.0", tk.END).strip()
        plaintext = ''
        codes_to_chars = {code: char for char, codes in self.key.items() for code in codes}
        i = 0
        while i < len(ciphertext):
            if ciphertext[i] == ' ':
                plaintext += ' '
            else:
                code = ciphertext[i:i+2]
                char = codes_to_chars.get(code)
                if char:
                    plaintext += char
                else:
                    plaintext += code
                i += 1
            i += 1
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", plaintext)

