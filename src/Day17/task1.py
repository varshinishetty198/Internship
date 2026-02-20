import sqlite3

conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
)
""")

cursor.execute("DELETE FROM interns")

intern_data = [
    ("Ananya", "Data Science", 15000),
    ("Rahul", "Web Dev", 12000),
    ("Priya", "AI/ML", 18000),
    ("Kiran", "Cyber Security", 14000),
    ("Meera", "Data Science", 16000)
]

cursor.executemany(
    "INSERT INTO interns (name, track, stipend) VALUES (?, ?, ?)",
    intern_data
)

conn.commit()

cursor.execute("SELECT name, track FROM interns")

rows = cursor.fetchall()

print("Intern Name and Track:")
print("-----------------------")

for row in rows:
    print(f" {row[0]} |  {row[1]}")

conn.close()