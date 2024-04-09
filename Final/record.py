import mysql.connector as conn

db = conn.connect(
    user = "root",
    host = "localhost",
    password = "admin@123",
    auth_plugin = "mysql_native_password",
    database = "final"
)

cur = db.cursor()
# cur_ins = "Insert into fin(name) values (%s)"

# cur_value = [("Ankit",),("Prakhar",),("Rahul",),("Daksh",)]

# cur.executemany(cur_ins,cur_value)

# print(cur.rowcount,"data inserted")

# db.commit()

# Update

# cur_up = "Update fin set name=%s where roll =%s"
# cur_value = [("Prakhar",7),("Ankit",11)]

# cur.executemany(cur_up,cur_value)
# print(cur.rowcount,"record updated")
# db.commit()


cur_up = "delete from fin where roll=%s"
cur_value = [(1,),(2,),(3,)]

cur.executemany(cur_up,cur_value)
print(cur.rowcount,"Delete successfully")
db.commit()