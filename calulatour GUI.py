import tkinter as tk
from tkinter import *


class Cal(tk.Tk):
    def __init__(self,):
        super().__init__()

        #these are the size of the window, its name and background colour.
        self.title("Calculator")
        self.geometry("200x300")
        self.creat_widgets()

    def creat_widgets(self):
        self.display = tk.Entry(self, font=("arial",24), bd=10, relief=tk.RIDGE, justify="right")
        self.display.grid(row=0,column=0,columnspan=4, ipadx=8,ipady=8)

        buttons = [("7","8","9","/"),
                   ("4","5","6","+"),
                   ("1","2","3","*"),
                   ("0",".","^","-"),
                   ("sin","cos","tan","sqrt"),
                   ("(",")","C","=")]
        for r, row in enumerate(buttons,1):
            for c, text in enumerate(row):
                button = tk.Button(self,text=text,font=("ariel",18),width=6,height=2)
                button.grid(row=r,column=c,padx=5,pady=5)
                button.config(command=self.create_command(text))

    def create_command(self,text):
        def command():
            self.button_click(text)
        return command
#this calls the window
window = Cal()
window.mainloop()