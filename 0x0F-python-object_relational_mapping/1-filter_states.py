#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the database."""
import MySQLdb
import sys

if __name__ == "__main__":
    """Connect to the database."""
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name RLIKE '^[N]' ORDER BY states.id")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
