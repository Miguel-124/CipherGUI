import tkinter as tk
import sys
class CaesarCipher(tk.Frame):

    def __init__(self, root):
        self.color1 = '#072b63'
        self.color2 = '#bfe2ff'
        self.color3 = '#89b9e1'

        self.letters = '#abcdefghijklmnopqrstuvwxyz'
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


