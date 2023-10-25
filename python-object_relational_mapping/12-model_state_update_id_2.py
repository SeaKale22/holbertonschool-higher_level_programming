#!/usr/bin/python3
"""change name od state id 2"""

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
    state_update = session.query(State)\
        .filter(State.id == 2)
    # query for specific state
    for state in state_update:
        state.name = "New Mexico"
        # change name
    session.commit()
    # commit changes
    session.close()
    # close session
