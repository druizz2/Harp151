#basic dropdown menu
from tkinter import *

root = Tk()
root.title("Dropdown practice")
root.geometry("400x400")

item_list = ["Yellow", "Blue", "Green", "Purple", "Violet", "Black", "Orange", "Pink", "Brown"]

def chosen_option():
    color = value.get()
    result_label = Label(root, text=f"You've chosen {color}")
    root.configure(background=color)
    result_label.pack()
    
value = StringVar()
value.set("Select a Color")
    
dropdown = OptionMenu(root, value, *item_list)
choose_button = Button(root, text="Click to choose", command=chosen_option)

dropdown.pack()
choose_button.pack()

root.mainloop()

