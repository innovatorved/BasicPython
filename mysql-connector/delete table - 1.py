import mysql.connector as pydb

mydb = pydb.connect(host = "localhost" , user="root" , passwd="7755011883" , database = "guptadb")

#creating a object
mycursor = mydb.cursor()

sql_querry = "delete from family where name = 'Ved Prakash Gupta'"

mycursor.execute(sql_querry)

mydb.commit()
