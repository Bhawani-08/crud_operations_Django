import mysql.connector as myconn

mydb = myconn.connect(
    host = "localhost",
    user = "root",
    password = "admin@123",
    database = "data1",
    auth_plugin = "mysql_native_password"
)

db_cursor = mydb.cursor()
db_insert = "Insert into Emp(empid,name,Department) values (%s,%s,%s)"
db_values = [(3,"ankit","Sales"),(4,"Daksh","Dev"),(5,"Prateek","sales")]
db_cursor.executemany(db_insert,db_values)
mydb.commit()

print(db_cursor.rowcount,"record Inserted")

