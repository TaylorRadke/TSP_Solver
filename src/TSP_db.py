import sys
import os.path as path
from reader import reader
from solver import greedy2opt
from output import output
import mysql.connector
import mysql.connector.errors as db_error
import re

def connection():
    try:
        return mysql.connector.connect(
            host="mysql.ict.griffith.edu.au",
            user="s5094922",
            password="hib9bkip",
            database="s5094922db"
        )
    except db_error.Error as e:
        print(e)
    return db

def main(args):
    # Connect to the database
    db_conn = connection()

    # Get all values from commandline, check if there is missing arguments
    try:
        problem = args[1]
        operation = args[2].upper()
        if (operation == "ADD" or operation == "SOLVE"):
            try:
                final = args[3]
            except IndexError as e:
                print(e)
    except IndexError as e:
        print(e)

    # Check if the problem provided matches the file for the problem
    if (operation == "ADD"):
        problem_file = re.match("([\w\d]*)",final).group()
        if (problem_file != problem):
            raise ValueError("Problem name does not match file name")
        else:
            reader(path.join(path.curdir,'..\\tsp_files',file_name),db_conn)

    if (operation == "")          

    # greedy2opt(tsp_node_dict, allowed_time)
    # output(tsp_node_dict)


if __name__ == "__main__": 
    main(sys.argv)



