import sqlite3
db_filename = 'todoroki.db'

conn = sqlite3.connect(db_filename)
"""
if db_filename:
    print('Need to create schema')
else:
    print('Database exists, assume schema does, too.')
conn.execute('drop table if exists staff')
print("Table staff Exists/Drop")
conn.execute('create table staff(ID int,Name text,Age int,Gender text)')
print("Table staff Created")
#insert Values
conn.execute('insert into staff(ID,Name,Age,Gender) values(0001,"Name 1",21,"M")')
conn.execute('insert into staff(ID,Name,Age,Gender) values(0002,"Name 2",28,"F")')
conn.execute('insert into staff(ID,Name,Age,Gender) values(0003,"Name 3",26,"M")')
conn.commit()
print("Rows are inserted in Table staff Created")
cursor = conn.cursor()
print("Displaying staff Created")
result = conn.execute('select * from staff')
for rows in result:
    print(rows)

result = conn.execute('select Name,age from staff where age>25')
for rows in result:
    print(rows)

conn.execute('drop table if exists student')
print("Table student Exists/Drop")
conn.execute('create table student(roll int,subject text,city text,phone int)')
print("Table student Created")
#insert Values
conn.execute('insert into student(roll,subject,city,phone) values(2,"science","kathmandu",9841234560)')
conn.execute('insert into student(roll,subject,city,phone) values(3,"maths","kathmandu",9851327860)')
conn.execute('insert into student(roll,subject,city,phone) values(4,"nepali","pokhara",9821360553)')
conn.commit()

print("Rows are inserted in Table student Created")
cursor = conn.cursor()

print("Displaying student Created")
cursor.execute('update student set city="patan"where phone is 9851327860')
result=cursor.fetchall()
result=cursor.fetchone()

result=conn.execute('select*from student')
for rows in result:
    print(rows)
"""    
print("Rows are inserted in Table student Created")
cursor = conn.cursor()

print("Displaying student Created")
cursor.execute('delete from student where phone is 9851327860')
result=cursor.fetchall()
result=cursor.fetchone()

result=conn.execute('select*from student')
for rows in result:
    print(rows)
