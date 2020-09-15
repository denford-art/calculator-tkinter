from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys

# create window
root = Tk()
root.title("Calculator")

# button's name
bttn_list = [
    "7", "8", "9", "+", "*",
    "4", "5", "6", "-", "/",
    "1", "2", "3", "(", ")",
    "0", ".", "±", "xⁿ",
    "Exit", "π", "sin", "cos",
    "C", "=", "n!", "√2", ]

# buttons
r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd = lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd, width=10).grid(row=r, column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1

# enter field
calc_entry = Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan=5)


# calculator logic
def calc(key):
    global memory
    if key == "=":
        # del word
        str1 = "-+0123456789.*/)("
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")
        # caltulate
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")

    # clear enter field
    elif key == "C":
        calc_entry.delete(0, END)

    # plus / minus
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass

    # enter pi
    elif key == "π":
        calc_entry.insert(END, math.pi)

    # exit from caltulator
    elif key == "Exit":
        root.after(1, root.destroy)
        sys.exit

    # enter exponentiation of a number
    elif key == "xⁿ":
        calc_entry.insert(END, "**")

    # enter sin or cos
    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))

    # enter "(" or ")"
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")

    # enter factorial of a number
    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))

    # enter sqrt from number
    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))

    # enter result
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


root.mainloop()
