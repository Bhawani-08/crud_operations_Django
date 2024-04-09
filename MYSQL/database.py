import mysql.connector as myconn

mydb = myconn.connect(
    host = "localhost",
    user = "root",
    password = "admin@123",
    auth_plugin = "mysql_native_password"
)

db_cursor = mydb.cursor()

db_cursor.execute("create database data1")

print("Database Created!!!")