#!/usr/bin/python3
"""
Prints the list of State objects
from the database hbtn_0e_6_usa
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: ./model_state.py <mysql_username> \
              <mysql_password> <database_name>")
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    print("{}: {}".format(state.id, state.name))