from functools import partial
import tkinter as tk
import random as rand
from tkinter import messagebox

global name_text_box
global health_text_box
global character_count

root = tk.Tk()

root.geometry("900x750")

root.title("DNDhelper v1.0 - Not Resizable")

root.resizable(False,False)

title = tk.Label(text="DNDHelper")

frame_height = 80

frame_list = []

'''
Features: DONE - Button that allows you to add a new character/NPC
          DONE - Text boxes that can store numbers
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

character_count = 0


###############################################################################################
# The Following code is not mine, and all credit goes to Sergeant_Ranger on github.           #
###############################################################################################



#MAIN FUNC
def create_scrollable_frame(x, y, scrollable_frame_width, scrollable_frame_height):
    container = tk.Frame(
        root, height=scrollable_frame_height, width=scrollable_frame_width
    )
    canvas_container = tk.Frame(
        container, height=scrollable_frame_height, width=scrollable_frame_width
    )

    result_canvas = tk.Canvas(canvas_container, width=scrollable_frame_width - 20)
    scroller = tk.Scrollbar(
        canvas_container, orient="vertical", command=result_canvas.yview
    )

    scrollable_frame = tk.Frame(result_canvas, width=scrollable_frame_width - 20)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: result_canvas.configure(scrollregion=result_canvas.bbox("all")),
    )

    result_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    result_canvas.configure(yscrollcommand=scroller.set)
    canvas_container.place(relheight=1, relwidth=1)
    scroller.pack(side="right", fill="y")
    result_canvas.pack(side="left", fill="both")

    container.place(x=x, y=y)

    def _on_mousewheel(event):
        result_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    scrollable_frame.bind_all("<MouseWheel>", _on_mousewheel)

    return scrollable_frame

#CREATE SCROLLABLE FRAME
global scrollable_frame
scrollable_frame = create_scrollable_frame(0, 0, 500, 650)

#TREAT SCROLLABLE FRAME AS AN OTHERWISE NORMAL FRAME

###############################################################################################
# Thanks again to Sergeant_Ranger for letting me use this.                                    #
###############################################################################################


# TODO: Add 70 character limit

def reposition_frames():
    curr_y = 0
    for frame in frame_list:
        frame.place(x=10, y=curr_y)
        curr_y += 80


class DestroyButton(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(command=self.callback)

    def callback(self):
        global character_count
        index = frame_list.index(self.master)
        frame_list.pop(index)
        self.master.destroy()
        reposition_frames()
        character_count -= 1
        scrollable_frame.configure(height = (len(frame_list)+1)*80)
        



def create_new_text(x, y, text, parent):
    text_box = tk.Text(parent, height=1, width=5)
    text_box.place(x=x, y=y)
    text_box.insert(tk.END, str(text))

def create_new_label(x, y, text, parent):
    label = tk.Label(parent, text=text, borderwidth=2, relief="solid")
    label.place(x=x, y=y)

def create_new_frame(x, y, width, height, name, health, armour):
    frame = tk.Frame(scrollable_frame, width=width, height=height, borderwidth=5, relief=tk.GROOVE)
    create_new_label(10, 0, name, frame)
    create_new_text(110+(int(len(name))*3), 0, health, frame)
    create_new_text(210+(int(len(name))*3), 0, armour, frame)
    destroy = DestroyButton(frame, text="Destroy Character")
    destroy.place(x=0, y=40)
    frame.place(x=x, y=y)
    frame_list.append(frame)

def create_new_character():
    global character_count
    name = name_text_box.get("1.0", "end-1c")
    health = health_text_box.get("1.0","end-1c")
    armour = armour_text_box.get("1.0","end-1c")
    scrollable_frame.configure(height= frame_height * (character_count+1))
    create_new_frame(10, (frame_height*character_count), 450, frame_height, name, health, armour)
    character_count += 1


# TODO: Add labels for different attributes.
# TODO: Add method to delete characters.


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