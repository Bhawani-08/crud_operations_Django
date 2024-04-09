# Herewe create a connectivity,create database , create table


import mysql.connector as conn

db = conn.connect(
    user = "root",
    host = "localhost",
    password = "admin@123",
    auth_plugin = "mysql_native_password",
    database = "final"
)
# print(db,"Connectivity established!!!!")

cur = db.cursor()

# cur.execute("create database final")
# print(cur.rowcount,"database created!!!!")
# cur.execute("CREATE TABLE fin ( `roll no.` int auto_increment, name varchar(10) )")
# cur.execute("CREATE TABLE fin ( `roll no.` int auto_increment primary key, name varchar(10) )")

cur.execute("create table fin(roll int auto_increment primary key,name varchar(10))")
print(cur.rowcount,"Table Created!!!")