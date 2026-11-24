import sqlite3

conn = sqlite3.connect("hospital.db")
cur = conn.cursor()
docName = input("Enter doctors name:")
typeDoc = ["GP", "Cardiologists", "Neurologists", "Radiologists",  "Dermatologists", "Oncologists"]
print(typeDoc)
docType = int(input("enter a value between 0-5:"))

docNum = input("Enter the doctors number:")
print(typeDoc)
print(typeDoc[docType])
# Insert ONE doctor record - explain what the ? ? ? are doing
cur.execute(
    "INSERT INTO doctors (name, type, phone) VALUES (?, ?, ?)",
    (docName, typeDoc[docType] , docNum)
    
    
)

conn.commit()
print("Inserted 1 doctor:", docName, typeDoc[docType] , docNum )

conn.close()
