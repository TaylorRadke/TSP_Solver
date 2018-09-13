import math
from time import time
import re
from queries import *
import sys
import mysql.connector.errors

def euclidean_distance(node1, node2):
    """Finds the euclidean distance between two nodes"""

    xd = abs(node1[1] - node2[1])
    yd = abs(node1[2] - node2[2])
    return math.sqrt(xd**2 + yd ** 2)


def tour_distance(tour):
    distance = 0
    for i in range(len(tour)-1):
        distance += euclidean_distance(tour[i], tour[i+1])
    return distance


def find_next_closest(tour):
    """Finds the next closest node"""

    shortest_route = euclidean_distance(tour[0],tour[1])
    index_closest_node = 1

    for i in range(2,len(tour)-1):
        check_route = euclidean_distance(tour[0],tour[i])
        if (check_route < shortest_route):
            shortest_route = check_route
            index_closest_node = i

    return index_closest_node


def greedy(tour):
    tour_list = []
    start_point = tour[0]

    while len(tour)-1 > 0:
        tour_list.append(tour[0])
        next_node_index = find_next_closest(tour)
        tour[0] = tour[next_node_index]
        tour.pop(next_node_index)

    tour.append(start_point)
    tour_list.append(tour[0])

    return tour_list


def transpose(tour,i,k):

    new_tour = []
    new_tour[0:i-1] = [tour[j] for j in range(0, i)]
    new_tour[i:k-1] = reversed(tour[i:k])
    new_tour[k:] = tour[k:]

    return new_tour


def solve(problem_name,db_conn,allowed_time):
    cur = db_conn.cursor()
    try:
        cur.execute(sql_get_nodes % problem_name)
        tour = greedy(cur.fetchall())
        
    except:
        print(problem_name + " does not exist in the database")

    print("Solving " + problem_name + " within " + str(allowed_time) + " seconds")

    improved = True
    tour.append(tour[0])
    start_time = time()

    def within_time():
        if time() - start_time <= allowed_time:
            return True
        else:
            return False

    def opt2(tour):
        best_distance = tour_distance(tour)
        if within_time():
            for i in range(1, len(tour)-2):
                if within_time():
                    for k in range(i+1,len(tour)):
                        new_tour = transpose(tour[:], i, k)
                        new_distance = tour_distance(new_tour)
                        if new_distance < best_distance:
                            tour = new_tour
                            best_distance = new_distance
        return tour
    try:
        while improved and within_time():
            s_tour = tour[:]
            tour = opt2(tour[:])
            if s_tour == tour:
                improved = False

        print("Solved " + problem_name + " in %.2f seconds" % (time()-start_time))
        print("Adding " + problem_name +" solution to database")

        cur.execute(sql_add_solution.format(problem_name,tour_distance(tour),allowed_time))

        for i in range(0,len(tour)-1):
            cur.execute(sql_add_solution_tour.format(
                name = problem_name,
                id = tour[i][0],
                runningtime = allowed_time,
                solve_order_id = i+1,
                x = tour[i][1],
                y = tour[i][2]
            ))
        db_conn.commit()
        print("Completed")

    except KeyboardInterrupt:
        print("Unexpected keyboard interrupt while adding solution to database")
        sys.exit(1)
    except mysql.connector.IntegrityError:
        print("Duplicate Error: Solution for {} with running time {} already exists in database".format(problem_name,allowed_time))
        sys.exit(1)



