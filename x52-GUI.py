from tkinter import *
from tkinter.ttk import *

window= Tk()
window.title('Welcome Chore')

def click():
    tech_2.configure(text="Button was clicked!")

def claw():
    box = Combobox(window)
    box['values'] =(1,2,3,4,5,'Other')
    box.current(5)
    box.grid(column=4,row=4)

tech_1 = Label(window, text='Hi',font=('Arial Black',50))
tech_1.grid(row=0,column=4)

box_2 = Combobox(window)
box_2['values'] = ('Enter')
box_2.current(0)
box_2.grid(column=1,row=0)

tech_2=Button(window,text='hey click me',command=claw)
tech_2.grid(row=0,column=3)

tech_3=Button(window,text='hey click me',command=click)
tech_3.grid(row=0,column=2)

window.mainloop()
