"""
Lori Walden
SDEV 140
"RollMaster: Dice-Flinging Delight"
This program will allow a user to choose what size and how many dice to roll 
(dice with sides of 4, 6, 8, 10, 12, 20, 100, or custom), 
and then output the results in a new window.
The program will only accept 0-50 in the spinboxes (for the quantities) and only positive
integers for the custom number of sides.
"""

# Import Modules Needed
import random            # To roll the dice
import sys               # To reset the program
import os                # To reset the program
import tkinter as tk     # To create the GUI
from tkinter import *    # To import all functions from tkinter
from tkinter import messagebox   # To create the alert window


# Create input/main window
root = tk.Tk()
root.title("RollMaster")


# Create instructions
intro_label = tk.Label(root, text="Please select the quantity of each dice")
intro_label.grid(row=0, column=0, columnspan=3)
intro2_label = tk.Label(root, text="you would like to roll (up to 50).")
intro2_label.grid(row=1, column=0, columnspan=3)
exp_label = tk.Label(root, text="Dice are identified by the number of sides - ")
exp_label.grid(row=2, column=0, columnspan=3)
exp2_label = tk.Label(root, text="a d4 has 4 sides and can roll 1-4.")
exp2_label.grid(row=3, column=0, columnspan=3)


# Function for input validation
def validate_input(value):
    if value.isdigit():
        if 0 <= int(value) <= 50:
            return True
    messagebox.showerror("Error", "Please enter a valid integer for the number of sides.")
    return
    
# Create labels and entry fields for input
  # d4
d4_label = tk.Label(root, text="Quantity of d4's: ")
d4_label.grid(row=5, column=0)
d4_entry = Spinbox(root, from_=0, to=50, width=3, validate="key", 
                        validatecommand=(root.register(validate_input), "%P"))
d4_entry.grid(row=5, column=1)
d4_image = PhotoImage(file="d4_50.gif")
d4_img = Label(root, image=d4_image)
d4_img.grid(row=5, column=2)

  # d6
d6_label = tk.Label(root, text="Quantity of d6's: ")
d6_label.grid(row=6, column=0)
d6_entry = Spinbox(root, from_=0, to=50, width=3, validate="key", 
                        validatecommand=(root.register(validate_input), "%P"))
d6_entry.grid(row=6, column=1)
d6_image = PhotoImage(file="d6_50.gif")
d6_img = Label(root, image=d6_image)
d6_img.grid(row=6, column=2)

  # d8
d8_label = tk.Label(root, text="Quantity of d8's: ")
d8_label.grid(row=7, column=0)
d8_entry = Spinbox(root, from_=0, to=50, width=3, validate="key", 
                        validatecommand=(root.register(validate_input), "%P"))
d8_entry.grid(row=7, column=1)
d8_image = PhotoImage(file="d8_50.gif")
d8_img = Label(root, image=d8_image)
d8_img.grid(row=7, column=2)

  # d10
d10_label = tk.Label(root, text="Quantity of d10's: ")
d10_label.grid(row=8, column=0)
d10_entry = Spinbox(root, from_=0, to=50, width=3, validate="key", 
                        validatecommand=(root.register(validate_input), "%P"))
d10_entry.grid(row=8, column=1)
d10_image = PhotoImage(file="d10_50.gif")
d10_img = Label(root, image=d10_image)
d10_img.grid(row=8, column=2)

  # d12
d12_label = tk.Label(root, text="Quantity of d12's: ")
d12_label.grid(row=9, column=0)
d12_entry = Spinbox(root, from_=0, to=50, width=3, validate="key", 
                        validatecommand=(root.register(validate_input), "%P"))
d12_entry.grid(row=9, column=1)
d12_image = PhotoImage(file="d12_50.gif")
d12_img = Label(root, image=d12_image)
d12_img.grid(row=9, column=2)

  # d20
d20_label = tk.Label(root, text="Quantity of d20's: ")
d20_label.grid(row=10, column=0)
d20_entry = Spinbox(root, from_=0, to=50, width=3, validate="key", 
                        validatecommand=(root.register(validate_input), "%P"))
d20_entry.grid(row=10, column=1)
d20_image = PhotoImage(file="d20_50.gif")
d20_img = Label(root, image=d20_image)
d20_img.grid(row=10, column=2)

  # d100
d100_label = tk.Label(root, text="Quantity of d100's: ")
d100_label.grid(row=11, column=0)
d100_entry = Spinbox(root, from_=0, to=50, width=3, validate="key", 
                        validatecommand=(root.register(validate_input), "%P"))
d100_entry.grid(row=11, column=1)

  # d custom
custom_header_label = tk.Label(root, text="Custom", font='bold')
custom_header_label.grid(row=12, column=0, columnspan=3)
custom_sides_label = tk.Label(root, text="Number of sides: ")  
custom_sides_label.grid(row=13, column=0)
custom_sides_entry = tk.Entry(root, width=5)
custom_sides_entry.grid(row=13, column=1)
custom_quantity_label = tk.Label(root, text="Quantity of dice to roll: ")
custom_quantity_label.grid(row=14, column=0)
custom_quantity_entry = Spinbox(root, from_=0, to=50, width=3, validate="key", 
                        validatecommand=(root.register(validate_input), "%P"))
custom_quantity_entry.grid(row=14, column=1)

custom_image = PhotoImage(file="custom_50.gif")
custom_img = Label(root, image=custom_image)
custom_img.grid(row=13, column=2, rowspan=2)


# Create a the results to be displayed later
result_text = Text(root, height=10, width=10)


# Function for rolling dice
def roll_dice():
    try:
        result_text.delete("1.0", tk.END)  # Clear previous text

        # Collect quantity and sides of dice
        dice_quantities = {
            4: int(d4_entry.get()),
            6: int(d6_entry.get()),
            8: int(d8_entry.get()),
            10: int(d10_entry.get()),
            12: int(d12_entry.get()),
            20: int(d20_entry.get()),
            100: int(d100_entry.get())
        }

        # Custom dice
        custom_sides = int(custom_sides_entry.get())
        custom_quantity = int(custom_quantity_entry.get())
        if custom_sides =="":
          pass
        elif custom_sides > 0 and custom_quantity > 0:
            dice_quantities[custom_sides] = custom_quantity
        else:                                     # If custom sides or quantity is invalid
            messagebox.showerror("Error", "Please enter a valid integer for the number of sides.")
            return
        # Roll dice and display results
        result = ""
        for sides, quantity in dice_quantities.items():
            if quantity > 0:
                rolls = [random.randint(1, sides) for _ in range(quantity)]
                result += f"{quantity} d{sides}'s: {rolls}\n"

        result_text.insert(tk.END, result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the number of sides.")
        return
    open_results_window()


# Function to open a new window with the results
def open_results_window():
    new_window = Toplevel()
    new_window.title("Results")
    intro_label = Label(new_window, text="You chose to roll: ")
    intro_label.grid(row=0, column=0, columnspan=2)
    result_label = Label(new_window, text=result_text.get("1.0", tk.END))
    result_label.grid(row=1, column=0, columnspan=2)
    # Buttons to Roll Again or Quit
    button_reset = Button(new_window, text="Reset", command=reset_program)
    button_reset.grid(row=3, column=0)
    button_quit = Button(new_window, text="Quit", command=root.quit)
    button_quit.grid(row=3, column=1)

# Function to reset program
def reset_program(): 
    python = sys.executable 
    os.execl(python, python, * sys.argv)

# Action buttons- Roll, Reset, Quit
button_roll = Button(root, text="Roll", command=roll_dice)
button_roll.grid(row=22, column=0, columnspan=3)
button_reset = Button(root, text="Reset", command=reset_program)
button_reset.grid(row=23, column=0)
button_quit = Button(root, text="Quit", command=root.quit)
button_quit.grid(row=23, column=1)


# Start GUI
root.mainloop()
