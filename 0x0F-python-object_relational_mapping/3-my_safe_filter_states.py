#!/usr/bin/python3
"""safe from MySQL injections!"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Connect to database and run query"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    cur = conn.cursor()

    match = sys.argv[4]
    cur.execute("""SELECT * FROM states WHERE name LIKE %s""", (match, ))

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
