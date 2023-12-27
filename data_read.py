import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('coordinates.db')
cursor = conn.cursor()

# Execute a SELECT query to retrieve all data from the mouse_clicks table
cursor.execute('SELECT * FROM coordinates')

# Fetch all rows from the result set
rows = cursor.fetchall()

# Display the retrieved data
for row in rows:
    print(f"ID: {row[0]}, X: {row[1]}, Y: {row[2]}")

# Close the database connection
conn.close()
