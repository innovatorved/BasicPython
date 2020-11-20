from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import*
import gspread

from oauth2client.service_account import ServiceAccountCredentials

url = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\VED GUPTA\\Desktop\\PYTHON files\\data manager\\tecch_pro.json', url)

client = gspread.authorize(creds)
sheet = client.open('NEXT_IN').sheet1

window = tk.Tk()
window.title('Data Adder')
window.geometry('240x220') #set the window size
window.resizable(0,0) # set anybody resize window aor not
window.iconbitmap(r'C:\Users\VED GUPTA\Desktop\PYTHON files\data manager\book1.ico')

info = ''
Username = 'brothers'
Password = '7755011883'

def Sub():
    entry = user.get()
    private_id = pas.get()

    if Username == entry and private_id == Password:
        label.destroy()
        u.destroy()
        entry_user.destroy()
        p.destroy()
        entry_pas.destroy()
        but.destroy()
        Main_program()
    else:
        message('Warning!' , 'pls check the Username and Password \n!'+entry+'\n!'+private_id)

def message(a,b):
    tk.messagebox.showinfo(a,b)

icon = tk.PhotoImage(file = 'D:\\Icon\\book.png')
label = tk.Label(window , image = icon)
label.pack(side = 'top')

u = tk.Label(window, text = 'UserName:')
u.pack()

user = tk.StringVar()
entry_user = tk.Entry(window, width =22, textvariable = user )
entry_user.pack()

p = tk.Label(window, text = 'Password:')
p.pack()

pas = tk.StringVar()
entry_pas = tk.Entry(window,show='*', width =22, textvariable = pas )
entry_pas.pack()

but = tk.Button(window, text ='Submit' ,command = Sub)
but.pack()

def logout():
    window.destroy()

def Main_program(): 
            
    def student_data(User,num):
        value = 0
        #print('Yes')
        info = ''
        dd = sheet.get_all_records()
        l=len(dd)
        #print(l)
        #print(dd)
        for x in dd:
            #print('\n')
            value+=1
            if User in x['Name'] and User != '' or num == x['Enrollment Number']:
                value = 0
                for i in x:
                    data=str(i)+':\t'+str(x[i])
                    #print(data)
                    #print(type(data))
                    info+=data+'\n'
                #print(info)
                message('Student_Data',info)
                info = ''
            if value == len(dd):
                message('Not Avail !','Enter Correct Name \n'+str(User)+'\tData not Available')
        
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

        if User == 'owner_call7271':
            dat = sheet.get_all_records()
            with open('for_Owner.txt' , 'a') as f:
                f.write(str(dat))
            f.close()
            message('Done Sir','Data Succesfully Saved in a file')
        elif stu == 'Student_Data':
            student_data(User,num)


        elif len(lis[2]) == 10 and len(lis[0]) >= 3:
            a = 'Submitted'
            b = 'Data Succesfully Added'
            dat = sheet.get_all_records()

            l=len(dat)+2
            i=0
            if stu == 'tech Student':
                a_e = 'NEXT.IN001'+str(l-1)
            else:
                a_e = 'NEXT.IN002'+str(l-1)
            lis.append(a_e)
            for x in lis:
                i = i+1
                sheet.update_cell(l,i, x)
            message(a,b+'\tYour Enrollment is '+str(a_e))

            #del entry box
            str1.delete(0,tk.END)
            str2.delete(0,tk.END)
            str3.delete(0,tk.END)
            str4.delete(0,tk.END)

        else :
            a = 'Warning!'
            b = 'pls fill all mandatory field'
            message(a,b)
            window.destroy()
            
    #radio button
    usertype = tk.StringVar()
    rad1 = Radiobutton(window, text = 'tech Student', value = 'tech Student' ,variable = usertype)
    rad1.grid(row = 1,column = 0,sticky = tk.NE)

    rad2 = Radiobutton(window, text = 'non_tech Student', value = 'non_tech Student' ,variable = usertype)
    rad2.grid(row = 1,column = 1)

    rad = Radiobutton(window, text = 'Student_Data', value = 'Student_Data' ,variable = usertype)
    rad.grid(row = 0,column = 0)


    #label

    l1 = tk.Label(window, text = 'Name:')
    l1.grid(row = 2, column = 0,sticky =tk.W)

    l2 = tk.Label(window, text = 'Age:')
    l2.grid(row = 3, column = 0,sticky =tk.W)

    l3 = tk.Label(window, text = 'Mobile No.:')
    l3.grid(row = 4, column = 0, sticky =tk.W)

    l4 = tk.Label(window, text = 'Email Id:')
    l4.grid(row = 5, column = 0, sticky =tk.W)

    l5 = tk.Label(window, text = 'Gender:')
    l5.grid(row = 6, column = 0, sticky =tk.W)

    #entry
    Name = tk.StringVar()
    str1 = tk.Entry(window, width =22, textvariable = Name )
    str1.grid(row = 2, column = 1)

    Age = tk.StringVar()
    str2 = tk.Entry(window,width =22, textvariable = Age)
    str2.grid(row = 3, column = 1)

    Mobile = tk.StringVar()
    str3 = tk.Entry(window,width =22, textvariable = Mobile)
    str3.grid(row = 4, column = 1)

    Email = tk.StringVar()
    str4 = tk.Entry(window,width =22, textvariable = Email)
    str4.grid(row = 5, column = 1)

    #add combo box
    gender_var = tk.StringVar()
    Gender = Combobox(window, width =19 , textvariable = gender_var)
    Gender['values'] = ('Male', 'Female' , 'Other')
    Gender.current(0)
    Gender.grid(row = 6, column = 1)

    #checkbox
    click = tk.IntVar()
    terms = tk.Checkbutton(window, text = 'I Accept terms And Condition that is \ndata is fully Safe and privated. ',variable = click)
    terms.grid(row = 7, columnspan = 3)
        
    #button
    butt = tk.Button(window, text ='Submit' ,command = Submit)
    butt.grid(row = 8, column = 1)

    butt2 = tk.Button(window, text ='logOut' ,command = logout)
    butt2.grid(row = 8 , column = 0 ,sticky = tk.NW)


window.mainloop()
