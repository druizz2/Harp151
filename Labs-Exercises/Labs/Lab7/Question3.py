import io
import requests 
import json
from tkinter import * 
from tkinter import font
import random 
from tkinter import messagebox


# TK VAR, BUTTON, LABEL, FRAME, MESSAGEBOX, ENTRY

root = Tk()
root.geometry("600x700")
root.title("The Legend of Zelda Breath of the Wild: Quick Facts")

manual_type = StringVar()
manual_type.set("")

user_choice = StringVar()
user_choice.set("Categories")


user_name = StringVar()
user_name.set("")


category_list = ["creatures", "equipment", "materials", "monsters", "treasure"]

def get_facts(category, username):
    fact_text.delete("1.0", "end")
    facts = requests.get(f"https://botw-compendium.herokuapp.com/api/v3/compendium/category/{category}")
    facts_json = facts.json()
    data = facts_json["data"]
    all_index_numbers = len(data) # use this for loop
    description = data[all_index_numbers-1]["description"]
    name = data[all_index_numbers-1]["name"]
    image = data[all_index_numbers-1]["image"]
    text = f"| {name.upper()} | \n {description} \n \n Here is a link to the image of this fact: \n {image} \n \n {username}, did you know this fact?"
    fact_text.insert(END, text)
    fact_text.tag_config("tag_name", justify="center")   # centering the text in the textbox
    fact_text.tag_add("tag_name", "1.0", "end")
    
def click():
    chosen_category = user_choice.get()
    username = user_name.get()
    get_facts(chosen_category, username)

def clear():
    messagebox.askquestion("Form", "Are you sure you want to clear?")
    fact_text.delete("1.0", "end")


      

title_frame = Frame(root)    
title_frame.grid(row=0, column=2) 


category_frame = Frame(root)
category_frame.grid(row=1, column=2)

zelda_font = font.Font(family="Hylia Serif Beta", size=30)  # to see font, look at folder 
title_label = Label(title_frame, text="The Legend of Zelda: Quick Facts", font=zelda_font).pack()

name_label = Label(category_frame, text="Enter your name:").pack()
name_entry = Entry(category_frame, width=15, borderwidth=5, textvariable=user_name).pack()
name_button = Button(category_frame, text="Submit", command=click)

drop_label = Label(category_frame, text="Select a category:").pack() 
dropdown = OptionMenu(category_frame, user_choice, *category_list).pack()  

choose_button = Button(category_frame, text="Choose Category", command=click)
choose_button.pack(pady = 20)

fact_text = Text(root, height=12)    
fact_text.grid(padx=15,columnspan=5) 


button_clear_fact= Button(root, font=24, text="Clear Fact", command=clear)
button_clear_fact.grid(columnspan=15, padx = 15, pady=20)



button_close_window = Button(root, font = 24, text="Close Window", command=root.destroy)
button_close_window.grid(columnspan=15, padx = 15, pady=20)

root.mainloop()