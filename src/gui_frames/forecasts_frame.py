from tkinter import *
from tkinter import ttk

class Forecast_Frm:
    def __init__(self, gui, data) -> None:
        self.frame = ttk.Frame(gui, padding=10)
        self.data = data

    def setup(self):
        for i in range(len(self.data)):
            cur_frm = ttk.Frame(self.frame, width=100, height=100, padding=15)
            ttk.Label(cur_frm, text=self.data[i].info()["time"]).pack()
            ttk.Label(cur_frm, text=self.data[i].info()["temp"]).pack()
            ttk.Label(cur_frm, text=self.data[i].info()["chance"]).pack()
            cur_frm.pack(side=LEFT)
    
    def pack(self):
        self.frame.pack()