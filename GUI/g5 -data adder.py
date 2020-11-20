from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import*
import gspread
from oauth2client.service_account import ServiceAccountCredentials

url = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\VED GUPTA\\Desktop\\PYTHON files\\data manager\\stu.json', url)

client = gspread.authorize(creds)
sheet = client.open('data_student').sheet1

def message(a,b):
    tk.messagebox.showinfo(a,b)
    

def Submit():
    stu = usertype.get()
    User = Name.get()
    Age_u = Age.get()
    num = Mobile.get()
    em = Email.get()
    gen = gender_var.get()

    if click.get() == 0:
        subs = 'NO'
    else :
        subs ='YES'
        
    lis =[User , Age_u , num , em , gen , subs , stu]

    if len(lis[2]) == 10 and len(lis[0]) >= 3:
        a = 'Submitted'
        b = 'Data Succesfully Added'
        with open('Database.txt' , 'a') as f:
            for x in lis:
                f.write(x + '\t')
            f.write('\n')
            f.close()
        dat = sheet.get_all_records()
        l=len(dat)+2
        i=0
        for x in lis:
            i = i+1
            sheet.update_cell(l,i, x)
        message(a,b)

        #del entry box
        str1.delete(0,tk.END)
        str2.delete(0,tk.END)
        str3.delete(0,tk.END)
        str4.delete(0,tk.END)

        
        
    else :
        a = 'Warning!'
        b = 'pls fill all mandatory field'
        message(a,b)
        l1.destroy()

        
window = tk.Tk()
window.title('Data Adder')
window.geometry('240x200') #set the window size
window.resizable(0,0) # set anybody resize window aor not
window.iconbitmap(r'C:\Users\VED GUPTA\Desktop\PYTHON files\data manager\book1.ico')
    
#radio button
usertype = tk.StringVar()
rad1 = Radiobutton(window, text = 'tech Student', value = 'tech Student' ,variable = usertype)
rad1.grid(row = 0,column = 0)

rad2 = Radiobutton(window, text = 'non_tech Student', value = 'non_tech Student' ,variable = usertype)
rad2.grid(row = 0,column = 1)

#label

l1 = tk.Label(window, text = 'Name:')
l1.grid(row = 1, column = 0,sticky =tk.W)

l2 = tk.Label(window, text = 'Age:')
l2.grid(row = 2, column = 0,sticky =tk.W)

l3 = tk.Label(window, text = 'Mobile No.:')
l3.grid(row = 3, column = 0, sticky =tk.W)

l4 = tk.Label(window, text = 'Email Id:')
l4.grid(row = 4, column = 0, sticky =tk.W)

l5 = tk.Label(window, text = 'Gender:')
l5.grid(row = 5, column = 0, sticky =tk.W)

#entry
Name = tk.StringVar()
str1 = tk.Entry(window, width =22, textvariable = Name )
str1.grid(row = 1, column = 1)

Age = tk.StringVar()
str2 = tk.Entry(window,width =22, textvariable = Age)
str2.grid(row = 2, column = 1)

Mobile = tk.StringVar()
str3 = tk.Entry(window,width =22, textvariable = Mobile)
str3.grid(row = 3, column = 1)

Email = tk.StringVar()
str4 = tk.Entry(window,width =22, textvariable = Email)
str4.grid(row = 4, column = 1)

#add combo box
gender_var = tk.StringVar()
Gender = Combobox(window, width =19 , textvariable = gender_var)
Gender['values'] = ('Male', 'Female' , 'Other')
Gender.current(0)
Gender.grid(row = 5, column = 1)

#checkbox
click = tk.IntVar()
terms = tk.Checkbutton(window, text = 'I Accept terms And Condition that is \ndata is fully Safe and privated. ',variable = click)
terms.grid(row = 6, columnspan = 3)

#button
butt = tk.Button(window, text ='Submit' ,command = Submit)
butt.grid(row = 7, column = 1)

window.mainloop()
