from tsp_gui import TSP_GUI_LOGIC
import wx
from lib.db import Database

if __name__ == "__main__": 
    app = wx.App(redirect=False)
    TSP_GUI_LOGIC(None,"tsp")
    app.MainLoop()
    


