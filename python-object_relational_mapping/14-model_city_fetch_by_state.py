#!/usr/bin/python3
"""lists all city objects"""

import sys
from model_state import Base, State
from model_city import City
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
    query = session.query(City, State)\
        .filter(City.state_id == State.id)\
        .order_by(City.id)\
        .all()
    # query for state id and city
    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
