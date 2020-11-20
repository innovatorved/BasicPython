import tkinter as tk

window = tk.Tk()
def left(event):
    label.configure(text = 'left clicked') 

def middle(event):
    label.configure(text = 'middle clicked')

def right(event):
    label.configure(text = 'right clicked') 
    
label = tk.Label(window, text = 'its find the pressed mouse key',fg = 'orange')
btn = tk.Button(window,text = 'click me', fg = 'lightblue', bg = 'blue')

#bind takes 2 parameters 1st is event and 2nd is function
btn.bind('<Button-1>', left)
btn.bind('<Button-2>', middle)
btn.bind('<Button-3>', right)

btn.pack()
label.pack()
window.mainloop()

