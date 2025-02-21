import tkinter as tk
from calculator import Calculator




class Cal(tk.Tk):
    def __init__(self,):
        super().__init__()

        #these are the size of the window, its name and background colour.
        self.title("Calculator")
        self.geometry("420x580")
        self.create_widgets()
        self.calculator = Calculator() #created the instance of calculator class
    #this function is called to create buttons for the GUI.
    def create_widgets(self):

        #self,display is where our numbers are going after clicking our numbers buttons and symbol buttons.
        self.display = tk.Entry(self, font=("arial",24), bd=10, relief=tk.RIDGE, justify="right")
        self.display.grid(row=0,column=0,columnspan=4, ipadx=4,ipady=4)

        #buttons is a list of list that we can use to create out widgets without having to do them all manually.
        buttons = [("7","8","9","/"),
                   ("4","5","6","+"),
                   ("1","2","3","*"),
                   ("0",".","^","-"),
                   ("sin","cos","tan","sqrt"),
                   ("(",")","C","=")]

        #this is a for loop that create and the buttons the first loop give them their place in the rows
        #and the second one give them the column to be placed.
        for r, row in enumerate(buttons,1):
            for c, text in enumerate(row):
                #this here are the way the buttons are created
                #first is the button creation where it created by using the list of lists and the for loop.

                button = tk.Button(self,text=text,font=("ariel",18),width=6,height=2)
                #second line is used to places the buttons through the two loops.
                button.grid(row=r, column=c, padx=5, pady=5)
                #the last line is the way to give the buttons the commands through the second for loop
                #command=lambda is used for the buttons to not do there command over and over without clicking.
                button.config(command=lambda t=text: self.calultour_buttons(t))

    #calulatour buttons are used to give the commands orders
    def calultour_buttons(self,text):
        #if you click the c buttons it delete everything in the display so you can begin again
        if text == "C":
            self.display.delete(0,tk.END)
        #this elif statement is used to calculate the numbers
        elif text == "=":
            try:
                #expression is used to get the calculations to this line
                expression = self.display.get()
                #result is used to calculate the equation.
                result = self.calculator.evaluate(expression)
                #this is used to delete the former expression to make room for the result
                self.display.delete(0,tk.END)
                #this adds the result to the display to show the answer
                self.display.insert(tk.END,result)

            #this exception for if the equation is impossible or not compatible impossible to do.
            except Exception:
                #delets equation form display so error is by itself
                self.display.delete(0, tk.END)
                #add error in display.
                self.display.insert(tk.END, "Error")
        #this else statement is used for the other buttons that aren't = or c
        else:
            #this is to get the current text in the display.
            current_text = self.display.get()
            #this display.delete is important without this,
            #if button is clicked the number will be continually added even if you don't click it again.
            self.display.delete(0, tk.END)
            #this line is adding the buttons text to the display.
            self.display.insert(tk.END, current_text + text)
#this calls the window
window = Cal()
window.mainloop()