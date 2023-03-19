#!/usr/bin/python3
""" lists all cities from the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Connect to the database and run queries"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    cur = conn.cursor()

    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id=cities.state_id""")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
