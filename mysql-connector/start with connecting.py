#importing mysql connector
import mysql.connector
mydb = mysql.connector.connect(host = "127.0.0.1" , user = "root" , passwd = "7755011883")

mycursor = mydb.cursor()
#print(mydb)

#check connection between mysql and python
if(mydb):
    print("Connected with MySQl !")

else:
    print("Not Connected With MySQl !")

mycursor.execute("USE nextin")
#mycursor.execute("SHOW TABLES")
mycursor.execute("describe data")

for db in mycursor:
    print(db)

'''

#mycursor.execute("USE nextin")
mycursor.execute("Select count(*) from nextin.login")

for db in mycursor:
    print(db)

mydb.commit()

mycursor.execute("create table nextin.data(Name varchar(20) , enroll_id varchar(15) , FathersName varchar(15))")

for db in mycursor:
    print(db)

    '''

#insert on any column in a table
inser = "insert into data(Name , enroll_id , FathersName) values (%s , %s, %s)"
dat = [("Ved Prakash Gupta" , "E17210" , "Ravindra Gupta") ,("Prakash Gupta" , "E18210" , "vindra Gupta") ]

mycursor.executemany(inser,dat)
mydb.commit()
