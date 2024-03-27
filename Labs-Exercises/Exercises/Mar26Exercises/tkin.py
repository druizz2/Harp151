from tkinter import * 

root = Tk() # root widget 
root.geometry("200x100") # Set the window size 

myLabel = Label(root, text = "Hello World") # going in the root widget
myLabel2 = Label(root, text = "Put new text here") 
myLabel.pack()  # puts on screen, very basic
myLabel2.pack()

root.mainloop() # keeps it open and running

