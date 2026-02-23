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

cur.execute("DELETE FROM interns") 

sample_data = [
    ("Varshini", "Data Science", 6000),
    ("Rahul", "Web Development", 4000),
    ("Anjali", "Data Science", 8000),
    ("Kiran", "AI/ML", 7000),
    ("Megha", "Web Development", 5500),
    ("Arun", "Data Science", 4500)
]

cur.executemany("""
INSERT INTO interns (name, track, stipend)
VALUES (?, ?, ?)
""", sample_data)

conn.commit()


print("\n--- Data Science interns with stipend > 5000 ---")
filter_query = """
SELECT * FROM interns
WHERE track = 'Data Science'
AND stipend > 5000;
"""
df_filter = pd.read_sql_query(filter_query, conn)
print(df_filter)


print("\n--- Average Stipend Per Track ---")
avg_query = """
SELECT track, AVG(stipend) AS average_stipend
FROM interns
GROUP BY track;
"""
df_avg = pd.read_sql_query(avg_query, conn)
print(df_avg)


print("\n--- Total Interns Per Track ---")
count_query = """
SELECT track, COUNT(*) AS total_interns
FROM interns
GROUP BY track;
"""
df_count = pd.read_sql_query(count_query, conn)
print(df_count)

conn.close()