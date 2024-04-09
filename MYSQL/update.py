import mysql.connector as myconn

mydb = myconn.connect(
    host = "localhost",
    user = "root",
    password = "admin@123",
    auth_plugin='mysql_native_password',
    database = "data1"
    
)

db_cursor = mydb.cursor()

up_value = "update Emp set empid=%s where name=%s"
set_value = ([2,"Rahul"],[1,"LC"])
db_cursor.executemany(up_value,set_value)
mydb.commit()
print("Updated Succesfully!!!")
