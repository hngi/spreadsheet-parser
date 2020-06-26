import mysql.connector
mydb =mysql.connector.connect(host="localhost", user="root", passwd="hng12345")

mycursor =mydb.cursor()

mycursor.execute("create database FGovDb")

mycursor.execute("show databases")
for db in mycursor:
    print(db)


