#add cmd used for data add
#stu_d cmd used for seeing attendence 
#na_d cmd used for print attendence sheet

from datetime import datetime
import time   
now=datetime.now()
time=now.strftime("%H:%M")
print(time)
b1=[12,40]
b2=[14,00]
b3=[17,00]

l=[['VED GUPTA','Electronic Engineering','E11033051','batch1',b1],['ANSH GUPTA','ELECTRICAL Engineering','E11023021','batch1',b1],['SANDEEP KUMAR','Electronic Engineering','E1103315','batch2',b2],['AJAY SHARMA',' CS','E12033023','batch3',b3],['ANCHAL','IT ','E11133047','batch3',b3],['SUDHANSHU SRIVASTAV','Civil Engineering','E11023032','batch2',b2]]
att=[]
dd=[]

while True:
    count=0
    a=input('Scan the info_')
    if a=='add':
        b=input('Enter the name of Student: ')
        c=input('Enter the branch of Student: ')
        d=input('Enter the Roll No. of Student: ')
        e =input('Enter the batch of student: ')
        dd=[b,c,d,e]
        if dd[3]=='batch1':
            dd.append(b1)
        elif dd[3]=='batch2':
            dd.append(b2)
        elif dd[3]=='batch3':
            dd.append(b3)
        else:
            print('pls enter correct batch\n')

        l.append(dd)
        print('Data Succesfully added')

    elif a=='stu_d':
        for x in range(0,len(att),1):
            print(att[x])

    elif a=='na_d':
        for x in range(0,len(name),1):
            print(dd[x])

    else:
        for x in range(0,len(l),1):
            if a in l[x]:
                print('\nStudent Name: ',l[x][0])
                print('Branch: ',l[x][1])
                print('Roll no.: ',l[x][2])
                print('batch: ',l[x][3])
                print('Timing: ',l[x][4][0],':',l[x][4][1])
                time=now.strftime("%M")
                t=now.strftime("%H")
                print('Current time: ',t,':',time)
                c=int(t)
                d=int(time)
                if c==l[x][4][0] and d>=l[x][4][1] and d<=(l[x][4][1]+15):
                    att.append(l[x])
                    dd.append(l[x][0])
                    print('Attendence done!\n')
                else:
                    print('sorry u are late \n')

            else:
                count+=1

        if count==len(l):
            print('Student not found_\n')
             
