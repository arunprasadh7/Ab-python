# Creating tables using python 

import sqlite3

conn = sqlite3.connect('C:\\Users\\arun\\Desktop\\Abdul Bari Python\\17 DataBase Connectivity\\univ.db')

cur = conn.cursor()

# creating department table
# cur.execute('create table Dept(deptno integer primarykey, name text)')

# creating Student table
cur.execute('create table Students(roll integer primarykey, name text, city text, deptno integer, foreign key(deptno) references Dept(deptno))')

conn.commit()

cur.close()

conn.close()