import tkinter as tk
from tkinter import ttk

from views.capture_frame import CaptureFrame
from views.controller_frame import ControllerFrame
from views.log_frame import LogFrame
from views.macro_frame import MacroFrame


class MainWindow:
    def __init__(self) -> None:
        self.__root = tk.Tk()
        root = ttk.Frame(self.__root, padding=10)
        root.pack()

        CaptureFrame(root).grid(row=0, column=0, columnspan=2)
        ControllerFrame(root).grid(row=1, column=0)
        MacroFrame(root).grid(row=1, column=1)
        LogFrame(root).grid(row=0, column=2, rowspan=2)

    def start(self):
        self.__root.mainloop()
