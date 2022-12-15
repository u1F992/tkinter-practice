import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk


class LogFrame(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)

        st = ScrolledText(self, width=30)
        st.pack()
