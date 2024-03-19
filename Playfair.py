import tkinter as tk

class PlayfairCipher(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.color1 = '#072b63'
        self.color2 = '#bfe2ff'
        self.color3 = '#89b9e1'
        self.key = 'KEYWORD'  # Przykładowe słowo kluczowe dla szyfru Playfair

        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(
            self,
            bg=self.color1,
            fg=self.color2,
            font=('Arial', 22, 'bold'),
            text='Playfair Cipher'
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

    def prepare_text(self, text):
        # Usuń spacje i zamień 'J' na 'I'
        text = text.upper().replace('J', 'I').replace(' ', '')
        # Dodaj dodatkową literę na końcu tekstu, jeśli jest nieparzysta
        if len(text) % 2 != 0:
            text += 'X'
        # Podziel tekst na pary liter
        pairs = [text[i:i + 2] for i in range(0, len(text), 2)]
        return pairs

    def generate_grid(self):
        grid = [['' for _ in range(5)] for _ in range(5)]
        key_index = 0
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Pomijamy 'J' z szyfru Playfair

        # Wypełnij siatkę kluczem
        for i in range(5):
            for j in range(5):
                if key_index < len(self.key):
                    grid[i][j] = self.key[key_index]
                    key_index += 1
                else:
                    # Jeśli klucz się skończył, uzupełnij resztę alfabetem
                    while alphabet:
                        letter = alphabet[0]
                        alphabet = alphabet[1:]
                        if letter not in ''.join(grid[i]) + ''.join(grid[j]):
                            grid[i][j] = letter
                            break
        return grid

    def find_position(self, grid, letter):
        for i in range(5):
            for j in range(5):
                if grid[i][j] == letter:
                    return i, j
        # Zwróć None tylko w przypadku, gdy znak nie znajduje się w siatce szyfru Playfair
        return None, None

    def encrypt_text(self):
        plaintext = self.text_widget.get("1.0", tk.END).strip()  # Usuń białe znaki na końcu tekstu
        pairs = self.prepare_text(plaintext)
        grid = self.generate_grid()
        ciphertext = ''

        for pair in pairs:
            row1, col1 = self.find_position(grid, pair[0])
            row2, col2 = self.find_position(grid, pair[1])

            if row1 is None or col1 is None or row2 is None or col2 is None:
                continue  # Pomijaj litery, które nie występują w siatce szyfru

            if row1 == row2:
                ciphertext += grid[row1][(col1 + 1) % 5] + grid[row2][(col2 + 1) % 5]
            elif col1 == col2:
                ciphertext += grid[(row1 + 1) % 5][col1] + grid[(row2 + 1) % 5][col2]
            else:
                ciphertext += grid[row1][col2] + grid[row2][col1]

        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", ciphertext)

    def decrypt_text(self):
        ciphertext = self.text_widget.get("1.0", tk.END).strip()  # Usuń białe znaki na końcu tekstu
        pairs = self.prepare_text(ciphertext)
        grid = self.generate_grid()
        plaintext = ''

        for pair in pairs:
            row1, col1 = self.find_position(grid, pair[0])
            row2, col2 = self.find_position(grid, pair[1])


            if row1 is None or col1 is None or row2 is None or col2 is None:
                continue  # Pomijaj litery, które nie występują w siatce szyfru

            if row1 == row2:
                plaintext += grid[row1][(col1 - 1) % 5] + grid[row2][(col2 - 1) % 5]
            elif col1 == col2:
                plaintext += grid[(row1 - 1) % 5][col1] + grid[(row2 - 1) % 5][col2]
            else:
                plaintext += grid[row1][col2] + grid[row2][col1]

        self.text_widget.delete("1.0", tk.END)

        self.text_widget.insert("1.0", plaintext)
