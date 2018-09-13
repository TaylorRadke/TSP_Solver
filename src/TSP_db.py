import sys
import os.path as path
from reader import reader
from solver import solve
from output import output
import mysql.connector
import re


def main(args):

    #### Define Absolute path to directory containing TSP problem files
    tsp_path = path.join("F:\\1810ICT_SoftwareDevelopmentProcesses\\tsp_solver\\tsp_files\\")


    # Connect to the database
    db_conn = connection()

    # Get problem name and problem operation values from commandline
    count = 0
    try:
        problem = args[1]
        count += 1
        operation = args[2].upper()
    except:
        print("Expected 2 argmuents, got {}".format(count))
        sys.exit(1)

    # Get third value, file if ADD and time if SOLVE   
    if (operation == "ADD" or operation == "SOLVE"):
        try:
            final = args[3]
        except IndexError:
            print("Expected 3 arguments, got 2")
            sys.exit(1)

    # Check if the problem provided matches the file for the problem
    if operation == "ADD":
        problem_file = re.match("([\w\d]*)",final).group()
        if (problem_file != problem):
            print("Value Error: Problem name does not match file name")
            sys.exit(1)
        else:
            reader(path.join(tsp_path,final),problem,db_conn)  

    elif operation.upper() == "SOLVE":
        if not float(final) < 0:
            solve(problem,db_conn,float(final))
        else:
            print("Solver time cannot be negative")

    elif operation.upper() == "FETCH":
        output(problem,db_conn)

def connection():
    """Connect to the database"""
    try:
        return mysql.connector.connect(
            host="mysql.ict.griffith.edu.au",
            user="s5094922",
            password="hib9bkip",
            database="s5094922db"
        )
    except:
        print("Failed to connect to the database")
        sys.exit(1)

if __name__ == "__main__": 
    main(sys.argv)



