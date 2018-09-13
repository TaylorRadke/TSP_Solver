from queries import *
import sys

def output(problem_name,db_conn):
    cur = db_conn.cursor(buffered=True)
    try:
        cur.execute(sql_get_min_tour.format(problem_name))

        distance = cur.fetchone()[0]
        
        cur.execute(sql_get_tour_of_running_time.format(problem_name,distance))

        time = cur.fetchone()[0]

        cur.execute(sql_fetch_best.format(problem_name,time))
        print(problem_name)
        print("Best Tour Distance Found: " + str(distance))
        j = 0
        print("Tour: ")
        for i in cur.fetchall():
            print(j)
            j += 1
    except:
        print("No solution for " + problem_name + " in the database")
    