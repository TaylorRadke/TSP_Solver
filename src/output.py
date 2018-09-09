def output(problem_name,db_conn):
    cur = db_conn.cursor(buffered=True)

    cur.execute(
        """Select min(TourLength)
        From Solutions
        Where Problem_Name = '{}' 
        ;""".format(problem_name))

    distance = cur.fetchone()[0]
    
    cur.execute("""
    Select RunningTime
    FROM Solutions
    Where Problem_Name = '{}'
    And TourLength = {};""".format(problem_name,distance))

    time = cur.fetchone()[0]

    sql_fetch_best = """ 
    Select Solve_Order_Id,x,y
    FROM Solution_Nodes
    Where Name = '{}'
    AND RunningTime = {}
    ;
    """
    cur.execute(sql_fetch_best.format(problem_name,time))

    print(problem_name)
    print("Best Tour Distance Found: " + str(distance))
    print("Tour: ")
    for i in cur:
        print(cur.fetchone())