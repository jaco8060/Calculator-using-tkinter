from ast import operator
from tkinter import *
root = Tk()

class calculator:
    def handler(self, e): #used to set enter key to equals button
        self.button_equal()
    def __init__(self, root):
        vcmd = (root.register(self.callback)) #for input validation (only allows numbers and operators)

        self.e = Entry(root, width =30, borderwidth=5, font="Calibri 16", validate='all', validatecommand=(vcmd, '%P'))
        self.e.grid(row=0,column=0, columnspan=3, padx= 10, pady = 10) # column span is to span all three columns underneath input
        self.e.focus()


        root.bind('<Return>',self.handler)
    
        button_1 = Button(root, text= "1",font ="Calibri 16 bold", padx=40, pady = 20, command= lambda: self.button_click(1))
        button_2 = Button(root, text= "2", font ="Calibri 16 bold",padx=40, pady = 20, command= lambda: self.button_click(2))
        button_3 = Button(root, text= "3", font ="Calibri 16 bold",padx=40, pady = 20, command= lambda: self.button_click(3))
        button_4 = Button(root, text= "4", font ="Calibri 16 bold",padx=40, pady = 20, command= lambda: self.button_click(4))
        button_5 = Button(root, text= "5", font ="Calibri 16 bold",padx=40, pady = 20, command= lambda: self.button_click(5))
        button_6 = Button(root, text= "6", font ="Calibri 16 bold",padx=40, pady = 20, command= lambda: self.button_click(6))
        button_7 = Button(root, text= "7",font ="Calibri 16 bold", padx=40, pady = 20, command= lambda: self.button_click(7))
        button_8 = Button(root, text= "8",font ="Calibri 16 bold", padx=40, pady = 20, command= lambda: self.button_click(8))
        button_9 = Button(root, text= "9",font ="Calibri 16 bold", padx=40, pady = 20, command= lambda: self.button_click(9))
        button_0 = Button(root, text= "0", font ="Calibri 16 bold",padx=40, pady = 20, command= lambda: self.button_click(0))

        button_add = Button(root, text= "+", font ="Calibri 16 bold",padx=40, pady = 20, command= self.add_current)
        button_clear = Button(root, text= "Clear", font ="Calibri 16 bold",padx=120, pady = 20, command= self.clear_current)
        button_equal = Button(root, text= "=", font ="Calibri 16 bold",padx=40, pady = 20, command= self.button_equal)
        button_multiply = Button(root, text= "*", font ="Calibri 16 bold",padx=40, pady = 20, command= self.button_multiply)
        button_divide = Button(root, text= "/", font ="Calibri 16 bold",padx=40, pady = 20, command= self.button_divide)
        button_subtract = Button(root, text= "-", font ="Calibri 16 bold",padx=40, pady = 20, command= self.button_multiply)
        button_percent = Button(root, text= "%", font ="Calibri 16 bold",padx=40, pady = 20, command= self.button_percent)
        button_bracket1 =  Button(root, text= "(", font ="Calibri 16 bold",padx=40, pady = 20, command= self.button_bracket1)
        button_bracket2 =  Button(root, text= ")", font ="Calibri 16 bold",padx=40, pady = 20, command= self.button_bracket2)
        button_decimal = Button(root, text= ".", font ="Calibri 16 bold",padx=40, pady = 20, command= self.button_decimal)
        button_backspace = Button(root, text= "Del", font ="Calibri 16 bold",padx=40, pady = 20, command= self.button_backspace)

        # put buttons on the screen//use sticky to remove gap between buttons

        button_1.grid(row=3, column=0, sticky="nsew")
        button_2.grid(row=3, column=1, sticky="nsew")
        button_3.grid(row=3, column=2, sticky="nsew")

        button_4.grid(row=2, column=0, sticky="nsew")
        button_5.grid(row=2, column=1, sticky="nsew")
        button_6.grid(row=2, column=2, sticky="nsew")

        button_7.grid(row=1, column=0, sticky="nsew")
        button_8.grid(row=1, column=1, sticky="nsew")
        button_9.grid(row=1, column=2, sticky="nsew")

        button_0.grid(row=4, column=0, sticky="nsew")

        button_equal.grid(row=4,column=2, sticky="nsew")
        button_decimal.grid(row=4,column=1, sticky="nsew")

        button_add.grid(row=6,column=0, sticky="nsew")
        button_multiply.grid(row=6,column=1, sticky="nsew")
        button_divide.grid(row=6,column=2, sticky="nsew")
        button_subtract.grid(row=7,column=0, sticky="nsew")
        button_backspace.grid(row=7,column=1, sticky="nsew")
        button_percent.grid(row=7,column=2, sticky="nsew")

        button_clear.grid(row=8,column=0,columnspan=3, sticky="nsew")
    def callback(self, P):
        if str.isdigit(P) or P == "" or "%" in P or "*" in P or "(" in P or ")" in P or "/" in P or "-" in P or "." in P or "ERROR" in P or "+" in P or "\n" in P:
            return True
        else:
            return False
    

    def button_backspace(self):
        current = self.e.get()
        temp = str(current)[:-1] # slice string to remove last letter
        self.e.delete(0, END) #replace old string with sliced string
        self.e.insert(0,temp)  # insert new number
    
    def button_click(self, number):
        # e.delete(0,END) # delete whats already in the box
        current = self.e.get()
        if (str(current) == "ERROR"): #delete ERROR when pressing a button then insert new number
            self.e.delete(0, END)
            self.e.insert(0,str(number))
        else: #if no error add number to number string
            self.e.delete(0, END)
            self.e.insert(0,str(current) + str(number))  # insert new number
        return

    def clear_current(self):
        self.e.delete(0, END)
        return

    def add_current(self):
        first_number = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0,first_number + str("+"))  # insert new number

    def button_multiply(self):
        first_number = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0,first_number + str("*"))  # insert new number
        return

    def button_divide(self):
        first_number = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0,first_number + str("/"))  # insert new number
        return

    def button_percent(self):
        first_number = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0,first_number + str("%"))  # insert new number
        return

    def button_bracket1(self):
        first_number = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0,first_number + str("("))  # insert new number
        return
    def button_bracket2(self):
        first_number = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0,first_number + str(")"))  # insert new number
        return

    def button_decimal(self):
        first_number = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0,first_number + str("."))  # insert new number
        return
    def button_backspace(self):
        current = self.e.get()
        temp = str(current)[:-1] # slice string to remove last letter
        self.e.delete(0, END) #replace old string with sliced string
        self.e.insert(0,temp)  # insert new number
        return

    def button_equal(self):

        current = self.e.get()
        try:
            equals = eval(str(current)) #let python evaluate the string
        except BaseException: # any error print out 'ERROR'
            self.e.delete(0,END) #clear whats in the box
            self.e.insert(0,str("ERROR"))
        else:

            self.e.delete(0,END) #clear whats in the box
            self.e.insert(0,equals) #insert answer
        return 

c = calculator(root)
root.title("Calculator")
root.mainloop()
