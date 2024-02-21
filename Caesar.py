import tkinter as tk
import sys
class CaesarCipher(tk.Frame):

    def __init__(self, root):
        self.color1 = '#072b63'
        self.color2 = '#bfe2ff'
        self.color3 = '#89b9e1'

        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.num_letters = len(self.letters)

        super().__init__(
            root,
            bg=self.color1
        )
        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.render_widgets()

    def render_widgets(self):
        self.title = tk.Label(
            self.main_frame,
            bg=self.color1,
            fg=self.color2,
            font=('Arial', 22, 'bold'),
            text='Caesar Cipher'
        )

        self.title.grid(column=0, row=0, sticky=tk.EW, pady=35)

        self.text_widget = tk.Text(
            self.main_frame,
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

        self.key_label = tk.Label(
            self.main_frame,
            bg=self.color1,
            fg=self.color2,
            font=('Arial', 13),
            text=f'Key (1-{self.num_letters -1})',
            justify=tk.CENTER
        )

        self.key_label.grid(column=0, row=2, pady=(38, 10))

        self.buttons_container = tk.Frame(self.main_frame, bg=self.color1)
        self.buttons_container.columnconfigure(0, weight=1)
        self.buttons_container.columnconfigure(1, weight=1)
        self.buttons_container.columnconfigure(2, weight=1)
        self.buttons_container.grid(column=0, row=3, sticky=tk.NSEW, padx=100)

        self.button_encript = tk. Button(
            self.buttons_container,
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
            state=tk.DISABLED
        )

        self.button_encript.grid(column=0, row=0, ipadx=5, ipady=5)

        self.button_decript = tk.Button(
            self.buttons_container,
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
            state=tk.DISABLED
        )

        self.button_decript.grid(column=2, row=0, ipadx=5, ipady=5)

        self.key_entry = tk.Entry(
            self.buttons_container,
            bg=self.color2,
            fg=self.color1,
            selectbackground=self.color1,
            selectforeground=self.color2,
            font=('Arial', 15),
            text='Encrypt',
            width=6,
            highlightthickness=0,
            border=0,
            justify=tk.CENTER
        )

        self.key_entry.grid(column=1, row=0, ipady=9)

    def encrypt_decrypt(self, text, mode, key): ...