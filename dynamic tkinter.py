# Import the required libraries
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the window
win.geometry("700x350")

def add_label():
   global label
   label=Label(win, text="1. A Newly created Label", font=('Aerial 18'))
   label.pack()

def remove_label():
   global label
   label.pack_forget()

def update_label():
   global label
   label["text"]="2. Yay!! I am updated"

# Create buttons for add/remove/update the label widget
add=ttk.Button(win, text="Add a new Label", command=add_label)
add.pack(anchor=W, pady=10)

remove=ttk.Button(win, text="Remove the Label", command=remove_label)
remove.pack(anchor=W, pady=10)

update=ttk.Button(win, text="Update the Label", command=update_label)
update.pack(anchor=W, pady=10)

win.mainloop()
