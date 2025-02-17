import tkinter as tk
from tkinter import *


class Cal(tk.Tk):
    def __init__(self,):
        super().__init__()

        #these are the size of the window, its name and background colour.
        self.title("Calculator")
        self.geometry("200x300")

        #this is where the equations go
        self.label = Label(text="")
        self.label.grid(row=0,column=0,sticky="w",padx=10, pady=10)

        #these buttons are the numbers buttons which add the numbers. through 1 to 0.
        self.button1 = Button(self, text="1",command=self.add_1)
        self.button1.grid(row=1,column=0, sticky="nsew")
        self.button2 = Button(self, text="2", command=self.add_2)
        self.button2.grid(row=1,column=1,sticky="nsew")
        self.button3 = Button(self, text="3", command=self.add_3)
        self.button3.grid(row=1,column=2,sticky="nsew")
        self.button4= Button(self, text="4", command=self.add_4)
        self.button4.grid(row=2,column=0,sticky="nsew")
        self.button5 = Button(self, text="5", command=self.add_5)
        self.button5.grid(row=2,column=1,sticky="nsew")
        self.button6 = Button(self, text="6", command=self.add_6)
        self.button6.grid(row=2,column=2,sticky="nsew")
        self.button7 = Button(self, text="7", command=self.add_7)
        self.button7.grid(row=3,column=0,sticky="nsew")
        self.button8 = Button(self, text="8", command=self.add_8)
        self.button8.grid(row=3,column=1,sticky="nsew")
        self.button9 = Button(self, text="9", command=self.add_9)
        self.button9.grid(row=3,column=2,sticky="nsew")
        self.button0 = Button(self, text="0", command=self.add_0)
        self.button0.grid(row=4,column=0,sticky="nsew")

        self.button_plus = Button(self,text="+",command=self.add_plus)
        self.button_plus.grid(row=1,column=4,sticky="nsew")
        self.button_minus = Button(self, text="-", command=self.add_minus)
        self.button_minus.grid(row=2, column=4, sticky="nsew")
    #these function are the commands the buttons uses when we click them.
    def add_1(self):
        space = self.label.cget("text")
        one = space + "1"
        self.label.config(text=one)
    def add_2(self):
        space = self.label.cget("text")
        two = space + "2"
        self.label.config(text=two)
    def add_3(self):
        space = self.label.cget("text")
        three = space + "3"
        self.label.config(text=three)
    def add_4(self):
        space = self.label.cget("text")
        four = space + "4"
        self.label.config(text=four)
    def add_5(self):
        space = self.label.cget("text")
        five = space + "5"
        self.label.config(text=five)
    def add_6(self):
        space = self.label.cget("text")
        six = space + "6"
        self.label.config(text=six)
    def add_7(self):
        space = self.label.cget("text")
        seven = space + "7"
        self.label.config(text=seven)
    def add_8(self):
        space = self.label.cget("text")
        eight = space + "8"
        self.label.config(text=eight)
    def add_9(self):
        space = self.label.cget("text")
        nine = space + "9"
        self.label.config(text=nine)
    def add_0(self):
        space = self.label.cget("text")
        zero = space + "0"
        self.label.config(text=zero)

    def add_plus(self):
        space = self.label.cget("text")
        plus = space + "+"
        self.label.config(text=plus)
    def add_minus(self):
        space = self.label.cget("text")
        minus = space + "-"
        self.label.config(text=minus)
#this calls the window
window = Cal()
window.mainloop()