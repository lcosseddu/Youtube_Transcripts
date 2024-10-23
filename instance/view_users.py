import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM user")
users = cursor.fetchall()

for user in users:
    print(user)

conn.close()