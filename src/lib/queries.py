sql_add_solution = """
    INSERT INTO Solution
    (ProblemName,TourLength,Date,Author,Algorithm,RunningTime,Tour)
    Values
    ('{name}',{length},CURDATE(),'Taylor','Greedy 2-opt',{runningtime},'{tour}');
    """

sql_get_cities = """
    SELECT ID,x,y from Cities
    WHERE Name = '{name}';
    """ 

sql_add_cities = """
    INSERT INTO Cities (Name,ID,x,y)
    Values
    ('{name}',{id},{x},{y});
    """

sql_get_solution = """
    SELECT TourLength,Tour
    FROM Solution
    WHERE ProblemName = '{name}'
    AND RunningTime = {runningtime}
    Limit 1;
    """

sql_add_problem = """
    INSERT INTO Problem (Name,Size,Comment)
    Values
    ('{name}',{size},'{comment}'); 
    """

sql_get_problem ="""
    SELECT * FROM Problem
    WHERE Name = '{name}';
    """