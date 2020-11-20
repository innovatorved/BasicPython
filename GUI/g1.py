import tkinter as tk

window = tk.Tk()
def save_txt():
    string = text_box.get()
    fx = open('file1','w')
    fx.write(string)
    fx.close()

text_box =tk.Entry(window) #text box adding
butt = tk.Button(window, text = "Save" , command = save_txt)

text_box.pack()
butt.pack()
window.mainloop()

