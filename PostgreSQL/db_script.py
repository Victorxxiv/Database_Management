import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Debugging: Print loades environment variables
print("DB Name:", os.getenv("PG_DB"))
print("User:", os.getenv("PG_USER"))
print("Password:", os.getenv("PG_PWD"))  # Be cautious with sensitive info in production
print("Host:", os.getenv("PG_HOST"))
print("Port:", os.getenv("PG_PORT"))

try:
    # Connect to PostgreSQL Database using environment variables
    conn = psycopg2.connect(
        dbname=os.getenv("PG_DB"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PWD"),
        host=os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT")
    )

    print("Connection established successfully.")
    # Create a cursor object using the cursor() method
    cur = conn.cursor()

    # Execute a SQL query using the execute() method
    cur.execute("SELECT * FROM users")

    # Fetch all of the rows from the query
    results = cur.fetchall()

    if not results:
        print("No results found.")
    else:
        # Print the results
        for row in results:
            print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()

except psycopg2.OperationalError as e:
    print("OperationalError: Could not connect to the database. Check your connection settings.")
    print(e)
except Exception as e:
    print("An error occurred:", e)
