from functools import partial
import tkinter as tk
import random as rand

global name_text_box
global health_text_box

root = tk.Tk()

root.geometry("750x750")

root.title("DNDhelper v1.0")

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


def create_new_text(x, y):
    text = tk.Text(root, height=1, width=5)
    text.place(x=x, y=y)

def create_new_label(x, y, text):
    label = tk.Label(root, text=text, borderwidth=2, relief="solid")
    label.place(x=x, y=y)

def create_new_character(x, y, name, health):
    print("New Character Created")
    print(name)


name_text_box_label = tk.Label(root, text="Name")
name_text_box_label.place(x=125, y=675)

name_text_box = tk.Text(root, height=1, width=5)
name_text_box.place(x=125,y=700)

health_text_box_label = tk.Label(root, text="Health")
health_text_box_label.place(x=200, y=675)

health_text_box = tk.Text(root, height=1, width=5)
health_text_box.place(x=200,y=700)



new_character_button = tk.Button(root, text="New Character", command=partial(create_new_character,5,5,"Orc1",5))
new_character_button.place(x=10,y=700)


root.mainloop()