#!/usr/bin/python3
"""List all cities of a state"""

import MySQLdb
import sys


def list_cities(username, password, database, state_name):
    """Lists all cities"""
    database_connection = MySQLdb.connect(host='localhost',
                                          user=username, passwd=password,
                                          db=database, port=3306)
    # conects to database
    cursor = database_connection.cursor()
    # make cursor
    qy = (
        "SELECT cities.name FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC")
    # make query
    cursor.execute(qy, (state_name,))
    # execute query
    city_names = [row[0] for row in cursor.fetchall()]
    city_string = ', '.join(city_names)
    print(city_string)

    cursor.close()
    database_connection.close()
    # close cursor and connection to database


if __name__ == "__main__":
    # check if name is main
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    # get args
    list_cities(username, password, database, state_name)
    # list cities
