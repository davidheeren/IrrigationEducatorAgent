import sqlite3
from pathlib import Path

folder_path = Path(__file__).parent.parent.joinpath("data")
folder_path.mkdir(parents=True, exist_ok=True)
database_path = Path(folder_path).joinpath("test.db")

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

# Create a table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
"""
)

name = "Mary Sue"
age = 21

# Insert data
# cursor.execute(
#     """
# INSERT INTO users (name, age) VALUES (?, ?)
# """,
#     (name, age),
# )

# Commit the changes
connection.commit()

# Retrieve data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

connection.close()
