import mysql.connector;

conn = mysql.connector.connect(db = 'workers', user = 'root', password = 'Coding20', host = 'localhost');

cursor = conn.cursor();

cursor.execute('select * from emp');

rows = cursor.fetchall();

print(rows);