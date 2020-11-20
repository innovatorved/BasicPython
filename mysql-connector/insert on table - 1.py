import mysql.connector as pydb

mydb = pydb.connect(host = "localhost" , user="root" , passwd="7755011883" , database = "guptadb")

#creating a object
mycursor = mydb.cursor()

#-------------sql querry for inserting values in tables
sql_querry = "insert into family(name , mobile_num) values(%s , %s)"

#-------------making tuple inside the list for inserting many row in table
family_mem = [("Ved Prakash Gupta" , 727101) , ("Ravindra Gupta" , 9451611) , ]

#--------------mycursor.executemany() _used for executing more than cmd
mycursor.executemany( sql_querry , family_mem)

#------------commit() used for inserting value in mysql
mydb.commit()
