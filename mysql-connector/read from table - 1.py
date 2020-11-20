import mysql.connector as pydb

mydb = pydb.connect(host = "localhost" , user="root" , passwd="7755011883" , database = "guptadb")

#creating a object
mycursor = mydb.cursor()


#-----------------recieve details from table
mycursor.execute("select * from family")

#----------------store data in single variable

            #---------------mycursor.fetchone() -fetchone is used for fetching only single value one by one from table
fetch_detail1 = mycursor.fetchone()


#----------------print the fetchone value
print("print only single value by fetchone")
print(fetch_detail1)

for det in fetch_detail1:
    print(det)
