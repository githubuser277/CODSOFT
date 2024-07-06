#import
import tkinter
from tkinter import *
from tkinter import messagebox

#intialize variables
var = ""
A = 0
operator = ""

#defining functions for buttons to display the clicked button
def button_1_clicked():
    global var
    var = var + "1"
    the_data.set(var)
    
def button_2_clicked():
    global var
    var = var + "2"
    the_data.set(var)
     
def button_3_clicked():
    global var     
    var = var + "3"
    the_data.set(var)

def button_4_clicked():
    global var
    var = var + "4"
    the_data.set(var)

def button_5_clicked():
    global var
    var = var + "5"
    the_data.set(var)
     
def button_6_clicked():
    global var
    var = var + "6"
    the_data.set(var)
      
def button_7_clicked():
    global var
    var = var + "7"
    the_data.set(var)

def button_8_clicked():
    global var
    var = var + "8"
    the_data.set(var)

def button_9_clicked():
    global var
    var = var + "9"
    the_data.set(var)

def button_0_clicked():
    global var
    var = var + "0"
    the_data.set(var)

def button_add_clicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "+"
    var = var + "+"
    the_data.set(var)

def button_sub_clicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "-"
    var = var + "-"
    the_data.set(var)

def button_mul_clicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "*"
    var = var + "*"
    the_data.set(var)
    
def button_div_clicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "/"
    var = var + "/"
    the_data.set(var)
    
def button_equal_clicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "="
    var = var + "="
    the_data.set(var)
    
def button_C_clicked():
    global A
    global var
    global operator
    var = ""
    A = 0
    operator = ""
    the_data.set(var)
    
#function to display result
def res():
    global A
    global operator
    global var
    var2 = var
    if operator == "+":
        a = float((var2.split("+")[1]))
        x = A + a
        the_data.set(x)
        var = str(x)
    elif operator == "-":
        a = float((var2.split("-")[1]))
        x = A - a
        the_data.set(x)
        var = str(x)
    elif operator == "*":
        a = float((var2.split("*")[1]))
        x = A * a
        the_data.set(x)
        var = str(x)
    elif operator == "/":
        a = float((var2.split("/")[1]))
        if a == 0:
            messagebox.showerror("Division by 0 Not Allowed")
            A == ""
            var = ""
            the_data.set(var)
        else: 
            x = float(A/a)
            the_data.set(x)
            var = str(x)


#gui window
#labels
guiWindow = tkinter.Tk()
guiWindow.geometry("320x500+400+400")
#guiWindow.resizable(0, 0)
guiWindow.title("Calculator")

the_data = StringVar()
guiLabel = Label(
    guiWindow,
    text = "Label",
    anchor = SE,
    font = ("Cambria Math", 20),
    textvariable = the_data,
    bg = "#FFFFFF",
    fg = "#000000"
    )
guiLabel.pack(expand = True, fill = "both")

#frames
frame1 = Frame(guiWindow, bg = "#000000")
frame1.pack(expand = True, fill = "both")
frame2 = Frame(guiWindow, bg = "#000000")
frame2.pack(expand = True, fill = "both")
frame3 = Frame(guiWindow, bg = "#000000")
frame3.pack(expand = True, fill = "both")
frame4 = Frame(guiWindow, bg = "#000000")
frame4.pack(expand = True, fill = "both")

#buttons in respective frames
#frame1
button1 = Button(
    frame1,
    text = "1",
    font = ("Cambria", 22),
    relief = GROOVE,
    border = 0,
    command = button_1_clicked
    )
button1.pack(side = LEFT, expand = True, fill = "both")

button2 = Button(
    frame1,
    text = "2",
    font = ("Cambria", 22),
    relief = GROOVE,
    border = 0,
    command = button_2_clicked
    )
button2.pack(side = LEFT, expand = True, fill = "both")

button3 = Button(
    frame1,
    text = "3",
    font = ("Cambria", 22),
    relief = GROOVE,
    border = 0,
    command = button_3_clicked
    )
button3.pack(side = LEFT, expand = True, fill = "both")

buttonC = Button(
    frame1,
    text = "C",
    font = ("Cambria", 22),
    relief = GROOVE,
    border = 0,
    command = button_C_clicked
    )
buttonC.pack(side = LEFT, expand = True, fill = "both")


#frame 2
button4 = Button(
    frame2,
    text = "4",
    font = ("Cambria", 22),
    relief = GROOVE,
    border = 0,
    command = button_4_clicked
    )
button4.pack(side = LEFT, expand = True, fill = "both")

button5 = Button(
    frame2,
    text = "5",
    font = ("Cambria", 22),
    relief = GROOVE,
    border = 0,
    command = button_5_clicked
    )
button5.pack(side = LEFT, expand = True, fill = "both")

button6 = Button(
    frame2,
    text = "6",
    font = ("Cambria", 22),
    relief = GROOVE,
    border = 0,
    command = button_6_clicked
    )
button6.pack(side = LEFT, expand = True, fill = "both")

buttonAdd = Button(
    frame2,
    text = "+",
    font = ("Cambria", 22),
    relief = GROOVE,
    border = 0,
    command = button_add_clicked
    )
buttonAdd.pack(side = LEFT, expand = True, fill = "both")


#frame 3
button7 = Button(
    frame3,
    text = "7",
    font = ("Cambria", 22),
    relief = GROOVE,
    border = 0,
    command = button_7_clicked
    )
button7.pack(side = LEFT, expand = True, fill = "both")

button8 = Button(
    frame3,
    text = "8",
    font = ("Cambria", 22),
    relief = GROOVE,
    border = 0,
    command = button_8_clicked
    )
button8.pack(side = LEFT, expand = True, fill = "both")

button9 = Button(
    frame3,
    text = "9",
    font = ("Cambria", 22),
    relief = GROOVE,
    border = 0,
    command = button_9_clicked
    )
button9.pack(side = LEFT, expand = True, fill = "both")

buttonSub = Button(
    frame3,
    text = "-",
    font = ("Cambria", 22),
    relief = GROOVE,
    border = 0,
    command = button_sub_clicked
    )
buttonSub.pack(side = LEFT, expand = True, fill = "both")

#frame 4
buttonZero = Button(
    frame4,
    text = "0",
    font = ("Cambria", 22),
    relief = GROOVE,
    border = 0,
    command = button_0_clicked
    )
buttonZero.pack(side = LEFT, expand = True, fill = "both")

buttonMul = Button(
    frame4,
    text = "*",
    font = ("Cambria", 22),
    relief = GROOVE,
    border = 0,
    command = button_mul_clicked
    )
buttonMul.pack(side = LEFT, expand = True, fill = "both")

buttonDiv = Button(
    frame4,
    text = "/",
    font = ("Cambria", 22),
    relief = GROOVE,
    border = 0,
    command = button_div_clicked
    )
buttonDiv.pack(side = LEFT, expand = True, fill = "both")

buttonEqual = Button(
    frame4,
    text = "=",
    font = ("Cambria", 22),
    relief = GROOVE,
    border = 0,
    command = res
    )
buttonEqual.pack(side = LEFT, expand = True, fill = "both")

#run gui
guiWindow.mainloop()
