from tkinter import *

# Widgets:- GUI elements such as Button, textbox, label, images, etc.
# Windows:- Serves as a container to hold or contain the widgets
count = 0

def click():
    global count
    count+=1
    label1 = Label(window, text=inputBox.get(),font=('Times New Romen',12),relief=RAISED,bd=3,padx=10,pady=10)
    label1.pack()
    print("Button Clicked..", count)

window = Tk() # Instatiate an instance of a window

window.geometry('400x420') # Change the diamensions
window.title("Demo Window")

photoInLabel = PhotoImage(file='calc_logo.png')

# Set icon
# **Convert icon to Photo Image first
icon = PhotoImage(file='calc_logo.png')
window.iconphoto(True,icon)

# Change Backgroud Color
window.config(background="white")


# ------------------ADDING INPUT BOX-------------------------------

inputBox = Entry(window, width= 48)
inputBox.get()
inputBox.pack()

# ------------------ADDING BUTTON-------------------------------
button = Button(window,background="white" ,text="Submit",command=click,activebackground="white",activeforeground="black")
button.pack()


# ------------------ADDING LABEL -------------------------------

# OR
# label1.place(x=0,y=0)
# label1.config(background="white")


window.mainloop()  # Will Show the Window