# Python program to create a simple GUI 
# calculator using Tkinter 
 
# import everything from tkinter module 
from tkinter import *
 
# globally declare the anyinput variable 
anyinput = "" 
 
 
# Function to update anyinput 
# in the text entry box 
def press(var): 
    # point out the global anyinput variable 
    global anyinput 
 
    # concatenation of string 
    anyinput = anyinput + str(var) 
 
    # update the anyinput by using set method 
    equation.set(anyinput) 
 
 
# Function to evaluate the final expression 
def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
 
    # Put that code inside the try block 
    # which may generate the error 
    try: 
 
        global anyinput 
 
        # eval function evaluate the anyinput 
        # and str function convert the result 
        # into string 
        total = str(eval(anyinput)) 
 
        equation.set(total) 
 
        # initialize the anyinput variable 
        # by empty string 
        anyinput = "" 
 
    # if error is generate then handle 
    # by the except block 
    except: 
 
        equation.set(" error ") 
        anyinput = "" 
 
 
# Function to clear the contents 
# of text entry box 
def clear(): 
    global anyinput 
    anyinput = "" 
    equation.set("") 


 
# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk() 
 
    # set the background colour of GUI window 
    gui.configure(background="light pink") 
 
    # set the title of GUI window 
    gui.title("Calculator") 
 
    # set the configuration of GUI window 
    gui.geometry("200x225") 
 
    # StringVar() is the variable class 
    # we create an instance of this class 
    equation = StringVar() 
 
    # create the text entry box for 
    # showing the anyinput . 
    anyinput_field = Entry(gui, textvariable=equation) 
 
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    anyinput_field.grid(columnspan=5, ipadx=40)
 
    # create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed . 
    button1 = Button(gui, text=' 1 ', fg='black', bg='green', 
                    command=lambda: press(1), height=2, width=5) 
    button1.grid(row=5, column=0) 
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='green', 
                    command=lambda: press(2), height=2, width=5) 
    button2.grid(row=5, column=1) 
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='green', 
                    command=lambda: press(3), height=2, width=5) 
    button3.grid(row=5, column=2) 
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='green', 
                    command=lambda: press(4), height=2, width=5) 
    button4.grid(row=4, column=0) 
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='green', 
                    command=lambda: press(5), height=2, width=5) 
    button5.grid(row=4, column=1) 
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='green', 
                    command=lambda: press(6), height=2, width=5) 
    button6.grid(row=4, column=2) 
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='green', 
                    command=lambda: press(7), height=2, width=5) 
    button7.grid(row=3, column=0) 
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='green', 
                    command=lambda: press(8), height=2, width=5) 
    button8.grid(row=3, column=1) 
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='green', 
                    command=lambda: press(9), height=2, width=5) 
    button9.grid(row=3, column=2) 
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='green', 
                    command=lambda: press(0), height=2, width=5) 
    button0.grid(row=6, column=1) 
 
    plus = Button(gui, text=' + ', fg='black', bg='green', 
                command=lambda: press("+"), height=2, width=5) 
    plus.grid(row=2, column=3) 
 
    minus = Button(gui, text=' - ', fg='black', bg='green', 
                command=lambda: press("-"), height=2, width=5) 
    minus.grid(row=3, column=3) 
 
    multiply = Button(gui, text=' * ', fg='black', bg='green', 
                    command=lambda: press("*"), height=2, width=5) 
    multiply.grid(row=4, column=3) 
 
    divide = Button(gui, text=' / ', fg='black', bg='green', 
                    command=lambda: press("/"), height=2, width=5) 
    divide.grid(row=5, column=3) 
 
    equal = Button(gui, text=' = ', fg='black', bg='green', 
                command=equalpress, height=2, width=5) 
    equal.grid(row=6, column=3) 
 
    clear = Button(gui, text='C', fg='black', bg='green', 
                command=clear, height=2, width=5) 
    clear.grid(row=2, column='0') 

    button00 = Button(gui, text=' 00 ', fg='black', bg='green', 
                    command=lambda: press("00"), height=2, width=5) 
    button00.grid(row=6, column=0) 
 
    Decimal= Button(gui, text='.', fg='black', bg='green', 
                    command=lambda: press('.'), height=2, width=5) 
    Decimal.grid(row=6, column=2) 

    percent = Button(gui, text=' % ', fg='black', bg='green', 
                    command=lambda: press("/100"), height=2, width=5) 
    percent.grid(row=2, column=2) 

    self_square = Button(gui, text=' x² ', fg='black', bg='green', 
                    command=lambda: press("**2"), height=2, width=5) 
    self_square.grid(row=2, column=1) 

    # start the GUI 
    gui.mainloop() 