import mysql.connector as pydb

mydb = pydb.connect(host = "localhost" , user="root" , passwd="7755011883" , database = "guptadb")

#creating a object
mycursor = mydb.cursor()

#update table
sql_querry = "update family set mobile_num = 7755011 where name = 'Ved Prakash Gupta'"


#execute statement
mycursor.execute(sql_querry)

mydb.commit()
