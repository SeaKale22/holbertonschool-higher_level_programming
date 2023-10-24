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
    first_state = session.query(State).order_by(State.id).first()
    # query for states and sort
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
    session.close()
    # close session
