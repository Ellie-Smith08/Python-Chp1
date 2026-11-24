import sqlite3

# This will create the database file hospital.db if it does not exist.
conn = sqlite3.connect("hospital.db")

print("Database 'hospital.db' created (or opened) successfully.")

# Always close the connection
conn.close()
