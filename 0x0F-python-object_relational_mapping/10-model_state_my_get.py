#!/usr/bin/python3
"""
Prints the list of State objects
from the database hbtn_0e_6_usa
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: ./model_state.py <mysql_username> \
              <mysql_password> <database_name> <name>")
        sys.exit(1)

    name = sys.argv[4].split()[1]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)\
        .filter(State.name == name).order_by(State.id)

    if states:
        for state in states:
            print("{}: {}".format(state.id, state.name))
    else:
        print("Not found")
