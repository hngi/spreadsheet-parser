import mysql.connector
mydb =mysql.connector.connect(host="localhost", user="root", passwd="hng12345", database="fgovdb")

mycursor =mydb.cursor()

mycursor.execute("create table expenses(code int(20), name varchar(200), monthAmt int(20), budget int(20), payment int(20), bal int(20))")

mycursor.execute("show tables")

for  tb in mycursor:
    print(tb)