import mysql.connector as pydb

mydb = pydb.connect(host = "localhost" , user="root" , passwd="7755011883")

#creating a object
mycursor = mydb.cursor()

#----------creating a Database
#mycursor.execute("create database guptadb")

#----------and we show the database
mycursor.execute("show databases")

#----------with the help of for loop
for db in mycursor:
    print(db)
