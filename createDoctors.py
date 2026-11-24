import sqlite3

# Connect to the existing hospital.db
conn = sqlite3.connect("hospital.db")
cur = conn.cursor()

# Create the doctors table
cur.execute("""
CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    phone TEXT
)
""")

conn.commit()
print("Table 'doctors' created (if it didn't already exist).")

conn.close()
