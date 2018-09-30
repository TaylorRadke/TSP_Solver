import os.path as path
from lib.reader import READER
from lib.solver import solve
from lib.output import output
from lib.queries import *
from tsp_gui import TSP_GUI_LOGIC
from lib.db import Query
import wx

if __name__ == "__main__": 
    app = wx.App()
    TSP_GUI_LOGIC(None,"tsp")
    app.MainLoop()
    


