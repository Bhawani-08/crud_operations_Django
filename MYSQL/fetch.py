import mysql.connector 

db = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = "admin@123",
    auth_plugin = "mysql_native_password",
    # database = "data1"
)

db_cursor = db.cursor()

db_cursor.execute("select * from data1.Emp")
# db_select = db_cursor.fetchone()
# db_select = db_cursor.fetchall()
for my in db_cursor.fetchall():
    print(my)