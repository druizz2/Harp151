from tkinter import *
#very simple entry widget
#does not do anything, just the framing

root = Tk()

label_user = Label(root, text="Username").pack()
entry_user = Entry(root, width=35, borderwidth=5).pack()
label_pass = Label(root, text="Password").pack()
entry_pass = Entry(root, width=35, borderwidth=5, show="*").pack()
label_pin_code = Label(root, text="Enter Pin").pack()
entry_pin = Entry(root, width=9, borderwidth=5, show="*").pack()
button = Button(root, font = 24, text = "Submit")
button.pack(pady = 20)

root.mainloop()


