import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import*

window = tk.Tk()
#User define function
def clicked():
    label.configure(text = 'Button was Clicked!')
    butt.configure(text = 'Clicked')

def clicked2():
    text = str.get()
    label.configure(text = text)
    butt2.configure(text = 'clicked')

def clicked3():
    #use of messahe box
    tk.messagebox.showinfo('my self','hlww gentle man i am VED')  #(messgae title, message content)

#rename the title of the window
window.title('GUI Application')
window.geometry('500x500') #set the window size
window.resizable(0,0) # set anybody resize window aor not
window.iconbitmap(r'C:\Users\VED GUPTA\Desktop\PYTHON files\data manager\book1.ico')

#label in front using Label function 
label = tk.Label(window, text = 'Hlww World' ,font =("Arial Bold", 35), bg = 'light blue' , fg = 'blue')
label2 = tk.Label(window, text = 'Radio button' , fg = 'orange')

#button
butt = tk.Button(window, text = 'Enter', bg = 'Black' ,fg = 'White', command = clicked)
butt2 = tk.Button(window, text = 'click to show' , bg = 'lightgreen' , fg = 'orange' ,command = clicked2)
butt3 = tk.Button(window, text = 'click for secret message' ,fg ='red', command = clicked3)

#adding combo box using function Combobox
box = Combobox(window)
box['values'] = (1,2,3,4,5,'heyy')
box.current(3) #define ccurrent value

#Entry function used for entering a string
str = Entry(window)

#use of Radiobutton
#select one t a time
rad1 = tk.Radiobutton(window, text = 'Python', value = 1)
rad2 = tk.Radiobutton(window, text = 'java', value = 2)
rad3 = tk.Radiobutton(window, text = 'C++', value = 3)

#grid is used for set the position of an object
label.grid(column = 0,row = 0)
butt.grid(column = 0,row = 1)
butt2.grid(column = 1,row = 1)
butt3.grid(column = 4,row = 0)
str.grid(column = 1,row = 0)
box.grid(column = 0,row = 2)
label2.grid(column = 2,row = 3)
rad1.grid(column = 1,row = 4)
rad2.grid(column = 2,row = 4)
rad3.grid(column = 3,row = 4)

#pack is used for showing object in window
# if grid is predefined pack function not been used
'''
butt.pack()
butt2.pack()
label.pack()
str.pack()

'''
window.mainloop()
