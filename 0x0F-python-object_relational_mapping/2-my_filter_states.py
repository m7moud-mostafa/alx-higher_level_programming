#!/usr/bin/python3
"""lists states from the database"""


if __name__ == "__main__":
    import MySQLdb as sql
    import sys

    db = sql.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name='{}' \
             ORDER BY id ASC".format(sys.argv[4])
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
