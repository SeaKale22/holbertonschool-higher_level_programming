#!/usr/bin/python3
"""delete all objects with an a"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # checks if name is main
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
        )
    # make engine to connect to database
    Session = sessionmaker(bind=engine)
    session = Session()
    # make session
    states_delete = session.query(State)\
        .filter(State.name.like('%a%'))
    # find states with an a
    for state in states_delete:
        # delete each state found
        session.delete(state)
    session.commit()
    # commit changes
    session.close()
    # close session
