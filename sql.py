import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info = """
    Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
    SECTION VARCHAR(25), MARKS INTEGER, ROLLNO INTEGER PRIMARY KEY);
"""

cursor.execute(table_info)

# Insert data into the table

cursor.execute('''INSERT INTO STUDENT values('Likith', 'Data Science', 'A', 95, 1)''')
cursor.execute('''INSERT INTO STUDENT values('Dehesh', 'Machine Learning', 'A', 96, 2)''')
cursor.execute('''INSERT INTO STUDENT values('Hari Krishna', 'Full Stack Development', 'A', 98, 3)''')
cursor.execute('''INSERT INTO STUDENT values('Sowmya', 'Full Stack Development', 'B', 98, 4)''')
cursor.execute('''INSERT INTO STUDENT values('Rushitha', 'AI', 'B', 97, 5)''')
cursor.execute('''INSERT INTO STUDENT values('Reena', 'AI', 'B', 97, 6)''')
cursor.execute('''INSERT INTO STUDENT values('Sravya', 'Data Analyst', 'B', 99, 7)''')
cursor.execute('''INSERT INTO STUDENT values('Karthik', 'Machine Learning', 'B', 96, 8)''')

# Display all the records
print("The inserted records are: ")

data=cursor.execute(''' Select * from STUDENT ''')
for row in data:
    print(row)

## Close the Connection

connection.commit()
connection.close()