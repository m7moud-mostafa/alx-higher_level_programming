#!/usr/bin/python3
"""lists states from the database"""


if __name__ == "__main__":
	import MySQLdb as sql
	import sys


	db = sql._mysql.connect(username=sys.argv[0], password=sys.argv[1], database=argv[2], port=3306)

	cur = db.curser()
	rows = cur.execute("SELECT id FROM states")
	rows.fetchall()
