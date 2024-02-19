import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='')

print(mydb)

mycursor=mydb.cursor()

# mycursor.execute('create database StudDB')

# print('Worked')

mycursor.execute("use newdb")

# mycursor.execute("create table student(name varchar(20),age int , place varchar(20))")

# sql='insert into student(name,age,place) values("Joe",11,"xxx")'
# mycursor.execute(sql)
# mydb.commit()

mycursor.execute('select * from student')
# x=mycursor.fetchall()     #return all the datas from the table
x=mycursor.fetchone()    #return only one row
print(x)