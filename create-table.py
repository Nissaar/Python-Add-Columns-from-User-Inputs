import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="password", #mysql server password
database="database" #mysql database name
)

mycursor = mydb.cursor()

table_name = input("Name of Table: ")
primary_key = input("Name of Primary Key: ")
datatype_of_primary_key = input("Datatype of Primary Key: ")
primary_key_method = input("Primary Key method to be used (AUTO_INCREMENT for example): ")

sql = "CREATE TABLE " + table_name + " (" +" "+ primary_key +" "+ datatype_of_primary_key +" "+ primary_key_method +" "+ "PRIMARY KEY);"

mycursor.execute(sql)

print("Table "+table_name+"has been successfully created with primary key "+primary_key)
