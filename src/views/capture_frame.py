import tkinter as tk
from tkinter import ttk


class CaptureFrame(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)

        CaptureSelector(self).grid(row=0, column=0)
        CaptureCanvas(self).grid(row=1, column=0)


def _get_capture_list():
    return ["hoge", "fuga", "piyo"]


def _set_capture(capture_index: int):
    print(f"capture initialized: {capture_index}")


class CaptureSelector(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)

        capture_list = _get_capture_list()
        selected = tk.StringVar()
        selected.set(capture_list[0])

        om = ttk.OptionMenu(self, selected, capture_list[0], *capture_list)
        om.config(width=40)
        btn = ttk.Button(self, text="OK",
                         command=lambda: _set_capture(capture_list.index(selected.get())))

        om.grid(row=0, column=0)
        btn.grid(row=0, column=1)


class CaptureCanvas(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master, padding=10)
        canvas = tk.Canvas(self, background="#000000")
        canvas.pack()
