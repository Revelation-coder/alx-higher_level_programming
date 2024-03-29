#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine and bind session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all State objects and sort by id
    states = session.query(State).order_by(State.id).all()

    # Print State objects
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
