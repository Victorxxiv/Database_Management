import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to PostgreSQL Database using environment variables
conn = psycopg2.connect(
    dbname=os.getenv("DBNAME"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    host=os.getenv("PG_HOST"),
    port=os.getenv("PG_PORT")
)

# Create a cursor object using the cursor() method
cur = conn.cursor()

# Execute a SQL query using the execute() method
cur.execute("SELECT FROM users WHERE email = %s", ('example@example.com',))

# Fetch all of the rows from the query
results = cur.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()