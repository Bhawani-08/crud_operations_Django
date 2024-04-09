import mysql.connector as myconn

mydb = myconn.connect(
    host = "localhost",
    user = "root",
    password = "admin@123",
    database = "data1",
    auth_plugin = "mysql_native_password"
)

db_cursor = mydb.cursor()

# db_delete = "delete from Emp where empid=%s"
# db_value = [(5)]
# db_cursor.execute(db_delete,db_value)
# mydb.commit()
# print("record deleted successfully!!!")

# --------------------------------------------------------------
# to delete the complete record we use truncate

db_delete = "truncate table Emp"
db_cursor.execute(db_delete)
mydb.commit()
print("Records delete successfully!!!!")
