import sys
sys.path.append('..')
from lib.queries import *
try:
    import mysql.connector
    import mysql.connector.errors
except ImportError:
    raise ImportError

class Database(object):
    def __init__(self):
        self.connection = self.connect()
        self.cursor = self.connection.cursor()

    def connect(self):
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
    
    def query(self,query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            raise e

    def insert(self,query):
        try:
            self.cursor.execute(query)
        except mysql.connector.Error as e:
            raise e

    def save(self):
        self.connection.commit()
    
    def close(self):
        self.connection.close()

class Query(Database):
    def __init__(self):
        super(Query,self).__init__()

    def addSolution(name,length,runningTime,tour):
        self.insert(sql_add_solution.format(
            name = name,
            length = length,
            runningtime = runningTime,
            tour = tour
        ))
    
    def addProblem(self,name,size,comment):
        self.insert(sql_add_problem.format(
            name = name,
            size = size,
            comment = comment
        ))
    
    def addCity(self,name,id,x,y):
        self.insert(sql_add_city.format(
            name = name,
            id = id,
            x = x,
            y = y
        ))

    def getCities(self,name):
        return self.query(sql_get_cities.format(
            name = name
        ))

    def getProblems(self):
        a = self.query(sql_get_problems)
        return [a[i][0] for i in range(len(a))]
        
    def getSolutionNames(self):
        a = self.query(sql_get_solutions)
        return [a[i][0] for i in range(len(a))]
    
    def getSolutionTimes(self,name):
        a = self.query(sql_get_solution_times.format(
            name = name
        ))
        return [str(a[i][0]) for i in range(len(a))]

    def getSolutionCities(self,name,runningtime):
        a =  self.query(sql_get_solution_cities.format(
            name = name,
            runningtime = runningtime
        ))
        b = a[0][0].split(',')
        return [int(i) for i in b]
    
    def getCity(self,name,_id):
        a = self.query(sql_get_city.format(
            name = name,
            id = _id
        ))

        return a
        
        