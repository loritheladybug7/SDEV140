"""
Lori Walden
SDEV 140
"RollMaster: Dice-Flinging Delight"
This program will allow a user to choose what size and how many dice to roll 
(dice with sides of 4, 6, 8, 10, 12, 20, 100, or custom), 
and then output the results in a new window.
"""

import random
import tkinter as tk
from tkinter import Button, Entry, Label, PhotoImage, Spinbox, Text, messagebox

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
        if custom_sides > 0 and custom_quantity > 0:
            dice_quantities[custom_sides] = custom_quantity

        # Roll dice and display results
        result = ""
        for sides, quantity in dice_quantities.items():
            if quantity > 0:
                rolls = [random.randint(1, sides) for _ in range(quantity)]
                result += f"Rolling {quantity} d{sides}'s: {rolls}\n"

        result_text.insert(tk.END, result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers.")

# Create input window
root = tk.Tk()
root.title("RollMaster: Dice-Flinging Delight")

# Create instructions
intro_label = tk.Label(root, text="Please select the quantity of each dice you would like to roll (up to 50).")
intro_label.grid(row=0, column=0, columnspan=2)
exp_label = tk.Label(root, text="Dice are identified by the number of sides - A d4 has 4 sides and can roll 1-4.")
exp_label.grid(row=1, column=0, columnspan=2)

# Create labels and entry fields for input
  # d4
d4_label = tk.Label(root, text="Quantity of d4's: ")
d4_label.grid(row=3, column=0)
d4_entry = Spinbox(root, from_=0, to=50, width=3)
d4_entry.grid(row=3, column=1)
d4_image = PhotoImage(file="d4_50.gif")
img = Label(root, image=d4_image)
img.grid(row=3, column=2)

  # d6
d6_label = tk.Label(root, text="Quantity of d6's: ")
d6_label.grid(row=4, column=0)
d6_entry = Spinbox(root, from_=0, to=50, width=3)
d6_entry.grid(row=4, column=1)

  # d8
d8_label = tk.Label(root, text="Quantity of d8's: ")
d8_label.grid(row=5, column=0)
d8_entry = Spinbox(root, from_=0, to=50, width=3)
d8_entry.grid(row=5, column=1)

  # d10
d10_label = tk.Label(root, text="Quantity of d10's: ")
d10_label.grid(row=6, column=0)
d10_entry = Spinbox(root, from_=0, to=50, width=3)
d10_entry.grid(row=6, column=1)

  # d12
d12_label = tk.Label(root, text="Quantity of d12's: ")
d12_label.grid(row=7, column=0)
d12_entry = Spinbox(root, from_=0, to=50, width=3)
d12_entry.grid(row=7, column=1)
d12_image = PhotoImage(file="d12_50.gif")
img = Label(root, image=d12_image)
img.grid(row=7, column=2)

  # d20
d20_label = tk.Label(root, text="Quantity of d20's: ")
d20_label.grid(row=8, column=0)
d20_entry = Spinbox(root, from_=0, to=50, width=3)
d20_entry.grid(row=8, column=1)
# image = PhotoImage(file="d20.png")
# img = Label(root, image=image, width=50, height=50)
# img.grid(row=8, column=2)

  # d100
d100_label = tk.Label(root, text="Quantity of d100's: ")
d100_label.grid(row=9, column=0)
d100_entry = Spinbox(root, from_=0, to=50, width=3)
d100_entry.grid(row=9, column=1)


  # d custom
custom_header_label = tk.Label(root, text="Custom")
custom_header_label.grid(row=10, column=0, columnspan=3)
custom_sides_label = tk.Label(root, text="Number of sides: ")  
custom_sides_label.grid(row=11, column=0)
custom_sides_entry = tk.Entry(root, width=5)
custom_sides_entry.grid(row=11, column=1)
custom_quantity_label = tk.Label(root, text="Quantity of dice to roll: ")
custom_quantity_label.grid(row=12, column=0)
custom_quantity_entry = Spinbox(root, from_=0, to=50, width=3)
custom_quantity_entry.grid(row=12, column=1)

# Action buttons
button_roll = Button(root, text="Roll", command=roll_dice)
button_roll.grid(row=22, column=0, columnspan=2)
button_reset = Button(root, text="Reset")   # Define reset function and link it here
button_reset.grid(row=23, column=0)
button_quit = Button(root, text="Quit", command=root.quit)
button_quit.grid(row=23, column=1)

# Label for output
# result_text = Text(root, height=10, width=50)
# result_text.grid(row=24, column=0, columnspan=2)

# Start GUI
root.mainloop()
