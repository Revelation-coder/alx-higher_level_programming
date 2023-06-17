#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username,
        passwd=password, db=database)
    cursor = db.cursor()

    # Prepare the SQL query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with user input
    cursor.execute(query, (search_name,))

    # Fetch all rows
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
