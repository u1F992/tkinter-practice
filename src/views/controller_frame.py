import tkinter as tk
from tkinter import ttk


class ControllerFrame(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)

        ControllerSelector(self).grid(row=0, column=0)


def _set_controller(port_name: str):
    print(f"controller initialized: {port_name}")


class ControllerSelector(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)

        port_name = tk.StringVar()
        port_name.set("0")

        label = ttk.Label(self, text="port name: ")
        entry = ttk.Entry(self, textvariable=port_name, width=10)
        btn = ttk.Button(
            self, text="OK", command=lambda: _set_controller(port_name.get()))

        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        btn.grid(row=0, column=3)
