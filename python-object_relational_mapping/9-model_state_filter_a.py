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
    # get args

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
        )
    # make engine to connect to database
    Session = sessionmaker(bind=engine)
    session = Session()
    # make session
    sa = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    # query for states and sort
    for state in sa:
        # print states
        print(f"{state.id}: {state.name}")
    session.close()
    # close session
