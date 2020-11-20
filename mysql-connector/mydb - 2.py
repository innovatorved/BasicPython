import mysql.connector as pydb

mydb = pydb.connect(host = "localhost" , user="root" , passwd="7755011883")

#check the connection
#print(mydb)

#verify conneeection by
if (mydb):
    print("Connection Succesfull !")

else:
    print("Connection UnSuccesfull !")
