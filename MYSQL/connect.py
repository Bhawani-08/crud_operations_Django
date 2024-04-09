import mysql.connector as myconn

mydb = myconn.connect(
    host = "localhost",
    user = "root",
    password = "admin@123",
    auth_plugin='mysql_native_password'
    
)

print(mydb,"Connection established...")
