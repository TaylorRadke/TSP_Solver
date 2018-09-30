import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import wx

class TSP_PLOT(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent,-1,size=(700,500),pos=(400,20))

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.figure = Figure()

        self.SetSizer(self.sizer)
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self,-1,self.figure)
        self.sizer.Add(self.canvas)
    
    def updatePlot(self,x,y):
        self.axes.clear()
        self.axes.plot(x,y)
        self.canvas = FigureCanvas(self,-1,self.figure)
   