#CRUD operations
import mysql.connector

mydb =mysql.connector.connect(host='localhost',user='root',passwd='password123')

print(mydb)
