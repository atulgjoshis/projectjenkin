import mysql.connector
mydb=mysql.connector.connect (
	host="mysql1",
	user="root",
	passwd="password",
	auth_plugin="mysql_native_password"
)

testcursor = mydb.cursor()

testcursor.execute("create database studentdb")

testcursor.execute("show databases")

for x in testcursor:
	print(x)
