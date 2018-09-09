import sys
import os.path as path
from reader import reader
from solver import greedy2opt
from output import output
import mysql.connector
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

def check_if_exists_in_db(problem,operation,db_conn):
 
    if (operation.upper() == "ADD"):
        cur = db_conn.cursor()
        try:
            cur.execute("Select * FROM Problem where Name = '{}';".format(problem))
        except mysql.connector.Error as e:
            raise e
        # except mysql.connector.DataError as e:
        #     raise e

        if (cur.fetchone() != None):
            return 

def main(args):
    # Connect to the database
    db_conn = connection()

    # Get problem name and problem operation values from commandline
    try:
        problem = args[1]
        operation = args[2].upper()
    except IndexError as e:
        raise e

    # Get third value, file if ADD and time if SOLVE   
    if (operation == "ADD" or operation == "SOLVE"):
        try:
            final = args[3]
        except IndexError as e:
            raise e

    # Check if the problem provided matches the file for the problem
    if (operation == "ADD"):
        problem_file = re.match("([\w\d]*)",final).group()
        if (problem_file != problem):
            raise ValueError("Problem name does not match file name")
        else:
            
            reader(path.join(path.curdir,'..\\tsp_files',final),problem,db_conn)    

    # greedy2opt(tsp_node_dict, allowed_time)
    # output(tsp_node_dict)


if __name__ == "__main__": 
    main(sys.argv)



