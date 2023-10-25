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

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
        )
    # make engine to connect to database
    Session = sessionmaker(bind=engine)
    session = Session()
    # make session
    new_state = State(name='Louisiana')
    # make new state object
    session.add(new_state)
    # add new object to session
    session.commit()
    # commit changes
    query = session.query(State)\
        .filter(State.name == 'Louisiana')
    # query for new stare
    for state in query:
        print(f"{state.id}")
    session.close()
    # close session
