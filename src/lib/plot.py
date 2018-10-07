import matplotlib as mlt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
import wx

class TSP_PLOT(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent,-1,size=(1000,1000),pos=(400,20))

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.figure = mlt.figure.Figure(dpi=None)

        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self,-1,self.figure)
        self.navbar = NavigationToolbar(self.canvas)
        
        self.sizer.Add(self.canvas)
        self.sizer.Add(self.navbar,wx.EXPAND|wx.LEFT)
        self.SetSizer(self.sizer)
        
        self.navbar.Realize()
        self.navbar.Realize()

    def updatePlot(self,name,tour):
        try:
            self.axes.clear()
            self.axes.set_title(name)
            self.axes.plot(self.getx(tour),self.gety(tour))
            self.canvas.draw()
        except IndexError:
            raise IndexError
    
    def getx(self,tour):
        a = [a[1] for a in tour]
        a.append(a[0])
        return a

    def gety(self,tour):
        a = [a[2] for a in tour]
        a.append(a[0])
        return a