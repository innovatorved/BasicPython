import tkinter as tk
def Submit():
    lab.destroy()

window = tk.Tk()
icon = tk.PhotoImage(file = 'D:\\Icon\\fire.png')
label = tk.Label(window , image = icon).grid(column=0)
lab = tk.Label(window , text = 'hey').grid(column=0)

butt = tk.Button(window, text ='Submit' ,command = Submit)
butt.grid(row = 7, column = 1)
window.mainloop()
