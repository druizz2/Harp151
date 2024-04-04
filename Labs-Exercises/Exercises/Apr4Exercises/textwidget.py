#basic text widget

from tkinter import *

root = Tk()
root.title("Dropdown practice")
root.geometry("500x500")

saved_text = StringVar()

def insert_text(text):
    test_widget.insert(END, text)

def clear_text():
    test_widget.delete("1.0", "end")
    
def save_text():
    saved_text = test_widget.get("1.0", "end-1c")
    Label(root, text=saved_text).pack()
    
test_widget = Text(root, font = ("Helvitica", "16"),
                  height=10, width=25)
test_widget.pack()

erase_button = Button(root, text="Erase Text", command=clear_text)
erase_button.pack(pady=20) 

save_button = Button(root, text="Save your text", command=save_text)
save_button.pack(pady=20)

insert_text("This is my initial text. I am trying out my Text widget for the first time!")

root.mainloop()


