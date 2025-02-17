import tkinter as tk
from tkinter import *


class Cal(tk.Tk):
    def __init__(self,):
        super().__init__()

        #these are the size of the window, its name and background colour.
        self.title("Calculator")
        self.geometry("200x300")


        self.label = Label(text="")
        self.label.pack()
        self.button = Button(self, text="1",command=self.add_1)
        self.button.pack()
    def add_1(self):

        space = self.label.cget("text")

        one = space + "1"

        self.label.config(text=one)


#this calls the window
window = Cal()
window.mainloop()