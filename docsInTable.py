import sqlite3

conn = sqlite3.connect("hospital.db")
cur = conn.cursor()

cur.execute("SELECT * FROM doctors")
rows = cur.fetchall()

print("All doctors in the table:\n")

for row in rows:
    # row is a *tuple: (id, name, type, phone)
    print(row)

conn.close()
