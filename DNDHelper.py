import tkinter as tk
import random as rand

root = tk.Tk()

'''
Features: Button that allows you to add a new character/NPC
          Text boxes that can store numbers
          Deal damage function?
          Categories for different attributes
          Auto-Roll function for initiative (NPCs only)
          Dice for additional rolling
'''

dice_list = [
    "D2",
    "D3",
    "D4",
    "D5",
    "D6",
    "D7",
    "D8",
    "D9",
    "D10",
    "D11",
    "D12",
    "D13",
    "D14",
    "D15",
    "D16",
    "D17",
    "D18",
    "D19",
    "D20"
]

current_die = tk.StringVar()

current_die.set(dice_list[4])


def create_new_text():
    text = tk.Text(root, height=1, width=5)
    text.pack()





root.mainloop()