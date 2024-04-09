import mysql.connector as myconn

mydb = myconn.connect(
    host = "localhost",
    user = "root",
    password = "admin@123",
    database = "data1",
    auth_plugin = "mysql_native_password"
)

db_cursor = mydb.cursor()
# db_cursor.execute("show tables")
db_cursor.execute("create table Emp(empid int, name varchar(25),Department varchar(25))")
print("Table created!!!")


# to know how many tables are there in a database we use

# for i in db_cursor:
#     print(i)