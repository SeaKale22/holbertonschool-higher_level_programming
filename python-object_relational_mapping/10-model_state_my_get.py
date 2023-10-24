#!/usr/bin/python3
"""lists all state objects"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # checks if name is main
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    # get args

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
        )
    # make engine to connect to database
    Session = sessionmaker(bind=engine)
    session = Session()
    # make session
    q = session.query(State)\
        .filter(State.name == state_name)\
        .order_by(State.id)
    # query for states and sort
    if q.count() == 0:
        print("Not found")
    for state in q:
        print(f"{state.id}")
    session.close()
    # close session
