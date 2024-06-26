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
    state = sys.argv[4].split()[0]
    query = "SELECT c.id, c.name, s.name FROM cities AS c \
             LEFT JOIN states AS s ON s.id = c.state_id \
             WHERE s.name='{}' \
             ORDER BY c.id ASC".format(state)

    cur.execute(query)
    rows = cur.fetchall()

    string = ""
    n_rows = len(rows)
    cities = [row[1] for row in rows]
    formatted_cities = ", ".join(cities)
    print(formatted_cities)
    cur.close()
    db.close()
