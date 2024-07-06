import random
from tkinter import *
from tkinter.ttk import *

#for password choice
def password_choice():
    entry.delete(0, END)
    length = var1.get()
    lower = "abcdefghijklmnopqrstuvxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    digits = "ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvxyz0123456789!@#$%^&*()"
    password = ""
    
    #if strength low
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("please choose an option")
        
#for password generation
def generate():
    password1 = password_choice()
    entry.insert(10, password1)
        
#main function
#create gui window
root = Tk()
var = IntVar()
var1 = IntVar()
root.resizable(0, 0)
root.title("Random Password Generator")

#label and entries
Random_password = Label(root, text = "Password")
Random_password.grid(row = 0)
entry = Entry(root)
entry.grid(row=0, column = 1)
c_label = Label(root, text = "Length")
c_label.grid(row = 1)

#buttons
generate_button = Button(root, text = "Generate", command = generate)
generate_button.grid(row = 0, column = 3)

#strength of password
radio_low = Radiobutton(root, text = "Low", variable = var, value = 1)
radio_low.grid(row = 1, column = 2, sticky = 'E')
radio_middle = Radiobutton(root, text = "Medium", variable = var, value = 0)
radio_middle.grid(row = 1, column = 3, sticky = 'E')
radio_strong = Radiobutton(root, text = "Strong", variable = var, value = 3)
radio_strong.grid(row = 1, column = 4, sticky = 'E')
combo = Combobox(root, textvariable = var1)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                   21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column = 1, row = 1)


#start gui
root.mainloop()
