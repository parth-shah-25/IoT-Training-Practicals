from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.geometry("800x800")
root.title('Images and Exit Button')

frame= Frame(root, width=500, height=500)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("calc_logo.png"))

label = Label(frame, image=img)
label.pack()

btnQuit = Button(root, text="Exit", command=root.quit)
btnQuit.pack()
root.mainloop()