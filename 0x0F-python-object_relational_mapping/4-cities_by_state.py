#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username,
        passwd=password, db=database)
    cursor = db.cursor()

    # Execute query to select all cities with their corresponding state names
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Fetch all rows
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
