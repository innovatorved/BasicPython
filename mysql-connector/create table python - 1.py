import mysql.connector as pydb

mydb = pydb.connect(host = "localhost" , user="root" , passwd="7755011883" , database = "guptadb")

#creating a object
mycursor = mydb.cursor()

#----------create table
#mycursor.execute("create table family(name varchar(25) , mobile_num int(10))")

#-----------show table
mycursor.execute("show tables")

#-----------show with the help of for loop
for tb in mycursor:
    print(tb)

