import matplotlib
import matplotlib as mlt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
import wx

class TSP_PLOT(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent,-1,size=(700,500),pos=(400,20))

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.figure = mlt.figure.Figure(dpi=None,figsize=(5,5))
        self.SetSizer(self.sizer)
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self,-1,self.figure)
        self.navbar = NavigationToolbar(self.canvas)
        self.navbar.Realize()

        self.sizer.Add(self.canvas, wx.EXPAND)
        self.sizer.Add(self.navbar,0,wx.LEFT | wx.EXPAND)
        
    
    def updatePlot(self,x,y):
        self.axes.clear()
        self.axes.plot(x,y)
        self.canvas = FigureCanvas(self,-1,self.figure)
        self.navbar = NavigationToolbar(self.canvas)