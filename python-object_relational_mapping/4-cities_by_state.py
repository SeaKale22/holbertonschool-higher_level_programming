#!/usr/bin/python3
"""List all cities"""

import MySQLdb
import sys


def list_cities(username, password, database):
    """Lists all cities"""
    database_connection = MySQLdb.connect(host='localhost',
                                          user=username, passwd=password,
                                          db=database, port=3306)
    # conects to database
    cursor = database_connection.cursor()
    # make cursor
    qy = (
        "SELECT cities.id, cities.name, states.name FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC")
    # make query
    cursor.execute(qy)
    # execute query
    for row in cursor.fetchall():
        # print each state
        print(row)

    cursor.close()
    database_connection.close()
    # close cursor and connection to database


if __name__ == "__main__":
    # check if name is main
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    # get args
    list_cities(username, password, database)
    # list cities
