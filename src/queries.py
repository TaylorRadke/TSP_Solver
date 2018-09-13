sql_add_solution_tour = """
    Insert into Solution_Nodes (Name,ID,RunningTime,Solve_Order_ID,x,y)
    Values ('{name}',{id},{runningtime},{solve_order_id},{x},{y});
    """

sql_add_solution = """
    INSERT INTO Solutions
    (Name,TourLength,Algorithm,RunningTime)
    Values
    ('{}',{},'Greedy 2-Opt',{});
    """

sql_get_nodes = """
    SELECT ID,x,y from Nodes
    where Name = '%s';
    """ 
sql_add_node = """
    INSERT INTO Nodes (Name,ID,x,y)
    Values ('{}',{},{},{});
    """

sql_get_min_tour = """
    Select min(TourLength)
    From Solutions
    Where Name = '{}' ;
    """

sql_get_tour_of_running_time = """
    Select RunningTime
    FROM Solutions
    Where Name = '{}'
    And TourLength = {};
    """

sql_fetch_best = """ 
    Select Solve_Order_Id,x,y
    FROM Solution_Nodes
    Where Name = '{}'
    AND RunningTime = {};
    """
sql_get_problems = """
    SELECT Name
    FROM Problems
    WHERE Name = '{}';
    """

sql_add_problem = """
    INSERT INTO Problems (Name,Dimension)
    Values ('{}',{}); 
    """