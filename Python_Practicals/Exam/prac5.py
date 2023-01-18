from tkinter import *

calculation = ""

def add_to_cal(number):
    global calculation
    calculation += str(number)
    textResult.delete(1.0,"end")
    textResult.insert(1.0,calculation)

def eval_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        textResult.delete(1.0,"end")
        textResult.insert(1.0,calculation)
        
    except:
        clear_field()
        textResult.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation =""
    textResult.delete(1.0,"end")


root = Tk()
# root.geometry("420x400")
root.title("Calculator")


textResult = Text(root,height=2, width=49, font=("Times New Roman", 14))
textResult.grid(columnspan=5)


# Creating Buttons

btn_0 = Button(root, text="0", padx=50,pady=20,command=lambda: add_to_cal(0))
btn_dot = Button(root, text=".", padx=52,pady=20,command=lambda: add_to_cal())
btn_mod = Button(root, text="%", padx=40,pady=20,command=lambda: add_to_cal("%"))

btn_2 = Button(root, text="2", padx=50,pady=20,command=lambda: add_to_cal(2))
btn_3 = Button(root, text="3", padx=50,pady=20,command=lambda: add_to_cal(3))
btn_1 = Button(root, text="1", padx=50,pady=20,command=lambda: add_to_cal(1))

btn_4 = Button(root, text="4", padx=50,pady=20,command=lambda: add_to_cal(4))
btn_5 = Button(root, text="5", padx=50,pady=20,command=lambda: add_to_cal(5))
btn_6 = Button(root, text="6", padx=50,pady=20,command=lambda: add_to_cal(6))

btn_7 = Button(root, text="7", padx=50,pady=20,command=lambda: add_to_cal(7))
btn_8 = Button(root, text="8", padx=50,pady=20,command=lambda: add_to_cal(8))
btn_9 = Button(root, text="9", padx=50,pady=20,command=lambda: add_to_cal(9))

btn_add = Button(root, text="+", padx=47,pady=20,command=lambda: add_to_cal("+"))
btn_sub = Button(root, text="-", padx=50,pady=20,command=lambda: add_to_cal("-"))
btn_mul = Button(root, text="*", padx=50,pady=20,command=lambda: add_to_cal("*"))
btn_div = Button(root, text="/", padx=50,pady=20,command=lambda: add_to_cal("/"))

btn_ac = Button(root, text="AC", padx=45,pady=20,command=clear_field)
btn_eqaulto = Button(root, text="=", padx=48,pady=20,command=eval_calculation)

btn_open = Button(root, text="(", padx=50,pady=20,command=lambda: add_to_cal("("))
btn_close = Button(root, text=")", padx=51,pady=20,command=lambda: add_to_cal(")"))

# Adding buttons
btn_0.grid(row=4,column=0)
# btn_dot.grid(row=4,column=1)
btn_mod.grid(row=4,column=2)

btn_1.grid(row=3,column=0)
btn_2.grid(row=3,column=1)
btn_3.grid(row=3,column=2)

btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)

btn_7.grid(row=1,column=0)
btn_8.grid(row=1,column=1)
btn_9.grid(row=1,column=2)

btn_add.grid(row=1,column=4)
btn_sub.grid(row=2,column=4)
btn_mul.grid(row=3,column=4)
btn_div.grid(row=4,column=4)

btn_ac.grid(row=4,column=1)
btn_eqaulto.grid(row=5,column=4)

btn_open.grid(row=5,column=0)
btn_close.grid(row=5,column=1)


root.mainloop()