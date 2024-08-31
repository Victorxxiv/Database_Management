import psycopg2

# Connect to PostgreSQL Database
conn = psycopg2.connect(
    dbname="victor_db",
    user="victor",
    password="PASSWORD",
    host="localhost",
    port="5432"
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