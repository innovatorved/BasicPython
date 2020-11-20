import mysql.connector as pydb

mydb = pydb.connect(host = "localhost" , user="root" , passwd="7755011883" , database = "guptadb")

#creating a object
mycursor = mydb.cursor()

#----------------print the fetchall value
    
            #---------------mycursor.fetchall() - fetchall is used for fetching all value from table.
mycursor.execute("select * from family")

fetch_all_detail1s = mycursor.fetchall()

print("print all value by fetchall")
print(fetch_all_detail1s)

for det in fetch_all_detail1s:
    print(det)
