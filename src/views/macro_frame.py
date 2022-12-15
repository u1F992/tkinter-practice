import tkinter as tk
from tkinter import ttk


class MacroFrame(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        MacroSelector(self).pack()


def _get_macro_list():
    return ["ほげ", "ふが", "ぴよ"]


def _start_macro(command):
    print(f"start macro: {command}")

class MacroSelector(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)

        macro_list = _get_macro_list()
        selected = tk.StringVar()
        selected.set(macro_list[0])

        om = ttk.OptionMenu(self, selected, macro_list[0], *macro_list)
        om.config(width=20)
        btn_reload = ttk.Button(self, text="Reload",
                         command=_get_macro_list)
        btn_start = ttk.Button(self, text="Start",
                         command=lambda: _start_macro(selected.get()))

        om.grid(row=0, column=0, columnspan=2)
        btn_reload.grid(row=1, column=0)
        btn_start.grid(row=1, column=1)

