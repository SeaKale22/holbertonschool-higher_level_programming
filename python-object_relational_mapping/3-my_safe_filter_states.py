#!/usr/bin/python3
"""Finds states by name"""

import MySQLdb
import sys

if __name__ == "__main__":
    # checks if code was not imported
    def list_states_name(username, password, database, state_name):
        """Finds state by name"""
        database_connection = MySQLdb.connect(host='localhost',
                                              user=username, passwd=password,
                                              db=database, port=3306)
        # conects to database
        cursor = database_connection.cursor()
        # make cursor
        qy = (
            "SELECT * FROM states "
            "WHERE name = %s "
            "ORDER BY states.id ASC")
        # make query
        cursor.execute(qy, (state_name,))
        # execute query
        for row in cursor.fetchall():
            # print each state
            if row[1] == state_name:
                print(row)
        cursor.close()
        database_connection.close()
        # close cursor and connection to database

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    # get args
    list_states_name(username, password, database, state_name)
