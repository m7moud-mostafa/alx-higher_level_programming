#!/usr/bin/python3
"""lists states from the database"""


if __name__ == "__main__":
	import MySQLdb as sql
	import sys


	db = sql._mysql.connect(
							username=sys.argv[1],
						 	password=sys.argv[2],
							database=sys.argv[3],
							port=3306,
							host= "localhost"
							)

	cur = db.curser()
	rows = cur.execute("SELECT * FROM states ORDER BY id ASC")
	rows.fetchall()

	for row in rows:
		print(row)

	cur.close()
	db.close()
