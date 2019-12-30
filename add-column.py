import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="password", #mysql server password
database="database" #mysql database name
)

mycursor = mydb.cursor()

table_name = input("Name of Table: ")

column_no = int(input("How many columns to be created ?"))

def add_column(table_name):
    column_name = input("Name of column: ")
    data_type = input("Datatype: ")
    sql1 = "ALTER TABLE " + table_name + " ADD " +column_name+" "+data_type+" ;"
    mycursor.execute(sql1)
    print(column_name + " Added Successfully")

for i in range(column_no):
    add_column(table_name)


check = input("Do you need more columns ? (y/n): ")

if check == "y" or check == "Y":
    more = int(input("How many more columns do you need ? : "))
    for i in range(more):
        add_column(table_name)
else :
    print("Columns added Successfully.")
