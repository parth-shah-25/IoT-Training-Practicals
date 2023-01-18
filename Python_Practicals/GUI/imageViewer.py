from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.geometry("800x800")

frame= Frame(root, width=1000, height=1000)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)


img = ImageTk.PhotoImage(Image.open("Images/Image5.jpg"))

label = Label(frame, image=img)
label.pack()

root.mainloop()
