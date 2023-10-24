#!/usr/bin/python3
"""lists all states starting with N from hbtn_0e_0_usa"""

import MySQLdb
import sys


def list_states_N(username, password, database):
    """Function to list states starting with N"""
    database_connection = MySQLdb.connect(host='localhost',
                                          user=username, passwd=password,
                                          db=database, port=3306)
    # connects to database
    cursor = database_connection.cursor()
    # make a cursor
    cq = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cursor.execute(cq)
    # get the states
    for row in cursor.fetchall():
        # print each state
        if row[1][0] == 'N':
            print(row)

    cursor.close()
    database_connection.close()
    # close cursor and connection to database


if __name__ == "__main__":
    # checks if code was not imported
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    # use args to get username, passs, and db name
    list_states_N(username, password, database)
