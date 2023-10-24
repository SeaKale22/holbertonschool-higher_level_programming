#!/usr/bin/python3
"""lists all states from hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # checks if code was not imported
    def list_states(username, password, database):
        """Function to list states"""
        database_connection = MySQLdb.connect(host='localhost',
                                              user=username, passwd=password,
                                              db=database, port=3306)
        # connects to database
        cursor = database_connection.cursor()
        # make a cursor
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        # get the states
        for row in cursor.fetchall():
            # print each state
            print(row)

        cursor.close()
        database_connection.close()
        # close cursor and connection to database

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    # use args to get username, passs, and db name
    list_states(username, password, database)
