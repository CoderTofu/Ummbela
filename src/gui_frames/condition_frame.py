from tkinter import ttk


class Condition_Frm:
    def __init__(self, gui, data) -> None:
        self.frame = ttk.Frame(gui, padding=10)
        self.data = data

    def setup(self):
        for i in range(len(self.data)):
            ttk.Label(self.frame, text=str(self.data[i])).pack()

    def pack(self):
        self.frame.pack()
        