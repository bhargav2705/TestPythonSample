import mysql.connector

conn = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='root')
print(conn.is_connected())

cursor = conn.cursor()
cursor.execute("select * from CustomerInfo")
rowAll = cursor.fetchall()
print(rowAll)
print(rowAll[2][0])
conn.close()
