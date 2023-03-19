#!/usr/bin/python3
"""lists all cities of that state, using the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Connect to the database and execute query"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    cur = conn.cursor()

    cur.execute(
        """SELECT name FROM cities WHERE state_id=
        (
            SELECT id FROM states WHERE name=BINARY '{}'
        )
        """.format(sys.argv[4])
    )

    query_rows = cur.fetchall()

    tmp = list(row[0] for row in query_rows)

    print(*tmp, sep=', ')

    cur.close()
    conn.close()
