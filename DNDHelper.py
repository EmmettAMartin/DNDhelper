from functools import partial
import tkinter as tk
import random as rand

global name_text_box
global health_text_box
global character_count

root = tk.Tk()

root.geometry("750x750")

root.title("DNDhelper v1.0 - Not Resizable")

root.resizable(False,False)

title = tk.Label(text="DNDHelper")

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

character_count = 1

def create_new_text(x, y, text):
    text_box = tk.Text(root, height=1, width=5)
    text_box.place(x=x, y=y)
    text_box.insert(tk.END, str(text))

def create_new_label(x, y, text):
    label = tk.Label(root, text=text, borderwidth=2, relief="solid")
    label.place(x=x, y=y)

def create_new_character():
    global character_count
    if character_count > 15:
        new_character_button["state"] = tk.DISABLED
    name = name_text_box.get("1.0", "end-1c")
    health = health_text_box.get("1.0","end-1c")
    armour = armour_text_box.get("1.0","end-1c")
    create_new_label(10, (40*character_count), text=name)
    create_new_text(110, (40*character_count), text=health)
    create_new_text(210, (40*character_count), text=armour)

    for i in range(3):
        #create_new_text()
        pass

    character_count += 1


name_text_box_label = tk.Label(root, text="Name")
name_text_box_label.place(x=125, y=675)

name_text_box = tk.Text(root, height=1, width=8)
name_text_box.place(x=125,y=700)

health_text_box_label = tk.Label(root, text="Health")
health_text_box_label.place(x=200, y=675)

health_text_box = tk.Text(root, height=1, width=8)
health_text_box.place(x=200,y=700)

armour_text_box = tk.Text(root, height=1, width=8)
armour_text_box.place(x=275,y=700)

armour_text_box_label = tk.Label(root, text="Armour")
armour_text_box_label.place(x=275, y=675)


new_character_button = tk.Button(root, text="New Character", command=create_new_character)
new_character_button.place(x=10,y=700)


root.mainloop()