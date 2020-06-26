import mysql.connector
mydb =mysql.connector.connect(host="localhost", user="root", passwd="hng12345", database="fgovdb")

mycursor =mydb.cursor()

sqlform = "insert into expenses(code,name,budget,monthAmt,payment,bal) values( %s, %s, %s, %s ,%s ,%s)"
expense = [("01", "Administration", 10000000, 800000, 200000, 900000), ("02", "Administration", 10000000, 800000, 200000, 900000),("03", "Administration", 10000000, 800000, 200000, 900000), ]
mycursor.executemany(sqlform, expense)

mydb.commit()