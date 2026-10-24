from tkinter import *
from tkinter import messagebox

# ---------------------------- BUTTON FUNTIONALITY ------------------------------- #
def button_input(value):
    user_input.insert(END, value)

def clear():
    user_input.delete(0, END)

def evaluate():
    try:
        nums_to_calc = user_input.get()
        result = eval(nums_to_calc)
        user_input.delete(0, END)
        user_input.insert(END, str(result))

    except NameError:
        messagebox.showinfo(title = "VALUE ERROR", message = "Alphabets and special symbols not allowed.\n " \
        "Please insert an integer or decimal number.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("TK CALCULATOR 🧮")
window.minsize(width = 500, height = 600)
window.config(padx = 50, pady = 50)

# Entry
user_input = Entry(width = 20, font = ("Arial", 20))
user_input.grid(column = 0, row = 0, columnspan = 4, sticky = "ew")
user_input.focus()

# NUMBER BUTTONS
# ROW 1 BUTTONS
no_7_button = Button(text = "7", width = 10, command = lambda: button_input(7))
no_7_button.grid(column = 0, row = 1)

no_8_button = Button(text = "8", width = 10, command = lambda: button_input(8))
no_8_button.grid(column = 1, row = 1)

no_9_button = Button(text = "9", width = 10, command = lambda: button_input(9))
no_9_button.grid(column = 2, row = 1)

division_button = Button(text = "/", width = 10, command = lambda: button_input("/"))
division_button.grid(column = 3, row = 1)

# ROW 2 BUTTONS
no_4_button = Button(text = "4", width = 10, command = lambda: button_input(4))
no_4_button.grid(column = 0, row = 2)

no_5_button = Button(text = "5", width = 10, command = lambda: button_input(5))
no_5_button.grid(column = 1, row = 2)

no_6_button = Button(text = "6", width = 10, command = lambda: button_input(6))
no_6_button.grid(column = 2, row = 2)

multiplication_button = Button(text = "*", width = 10, command = lambda: button_input("*"))
multiplication_button.grid(column = 3, row = 2)

# ROW 3 BUTTONS
no_1_button = Button(text = "1", width = 10, command = lambda: button_input(1))
no_1_button.grid(column = 0, row = 3)

no_2_button = Button(text = "2", width = 10, command = lambda: button_input(2))
no_2_button.grid(column = 1, row = 3)

no_3_button = Button(text = "3", width = 10, command = lambda: button_input(3))
no_3_button.grid(column = 2, row = 3)

subtraction_button = Button(text = "-", width = 10, command = lambda: button_input("-"))
subtraction_button.grid(column = 3, row = 3)

# ROW 4 BUTTONS
no_0_button = Button(text = "0", width = 10, command = lambda: button_input(0))
no_0_button.grid(column = 0, row = 4)

clear_button = Button(text = "CLEAR", width = 10, command = clear)
clear_button.grid(column = 1, row = 4)

equal_button = Button(text = "=", width = 10, command = evaluate)
equal_button.grid(column = 3, row = 5)

addition_button = Button(text = "+", width = 10, command = lambda: button_input("+"))
addition_button.grid(column = 3, row = 4)

decimal_point_button = Button(text = ".", width = 10, command = lambda: button_input("."))
decimal_point_button.grid(column = 2, row = 4)











for column in range(4):
    window.columnconfigure(column, weight = 1)

for row in range(5):
    window.rowconfigure(row, weight = 1)



window.mainloop()