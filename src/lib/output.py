
import sys
sys.path.append('..')
from lib.queries import *

def output(problem_name,db):
    a = db.query(sql_get_solution.format(name=problem_name,runningtime=1))
    print(a)
    