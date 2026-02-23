import sqlite3
import pandas as pd

conn = sqlite3.connect("interns.db")
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    track TEXT,
    stipend INTEGER
);
""")


cur.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mentor_name TEXT,
    track TEXT
);
""")


cur.execute("DELETE FROM interns")
cur.execute("DELETE FROM mentors")


intern_data = [
    ("Rahul", "Web Development", 4000),
    ("Anjali", "Data Science", 8000),
    ("Kiran", "AI/ML", 7000),
    ("Megha", "Data Science", 6000)
]

cur.executemany("""
INSERT INTO interns (name, track, stipend)
VALUES (?, ?, ?)
""", intern_data)


mentor_data = [
    ("Dr. Sharma", "Data Science"),
    ("Mr. Verma", "Web Development"),
    ("Ms. Iyer", "AI/ML")
]

cur.executemany("""
INSERT INTO mentors (mentor_name, track)
VALUES (?, ?)
""", mentor_data)

conn.commit()


join_query = """
SELECT 
    interns.name AS intern_name,
    interns.track,
    interns.stipend,
    mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
"""

df = pd.read_sql_query(join_query, conn)

print("Joined Data:\n")
print(df)


conn.close()