import wx
import matplotlib.pyplot as plt

class TSP_GUI(wx.Frame):
    def __init__(self,parent,title):
        super(TSP_GUI,self).__init__(parent,title=title,size=(960,500))
        self.panel = wx.Panel(self,id=wx.ID_ANY,size=(720,600))
        self.tours = []
        self.font = wx.Font(12,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)
        self.uploadProblemInterface()
        self.problemsInterface()
        self.solutionsInterface()
        

    def initialise(self):
        self.Show(True)    
        
    def uploadProblemInterface(self):
        self.__uploadLabel = wx.StaticText(self.panel,label="Upload Problem",pos=(5,20)).SetFont(self.font)

        self.addProblemInput = wx.TextCtrl(self.panel,pos=(5,50))
        self.addProblemSubmit = wx.Button(self.panel,label="Submit",pos=(125,50))
        self.Bind(wx.EVT_BUTTON,self.uploadProblem,self.addProblemSubmit)


    def problemsInterface(self):
        self.__problemsLabel = wx.StaticText(self.panel,label="Problems",pos=(5,100)).SetFont(self.font)

        self.problemsList = wx.ComboBox(self.panel,choices=self.tours, pos=(5,125),size=(130,125))
        self.Bind(wx.EVT_COMBOBOX,self.onSelect,self.problemsList)


    def solutionsInterface(self):
        self.__solutionsLabel = wx.StaticText(self.panel,label="Solutions",pos=(5,300)).SetFont(self.font)

    def onSelect(self,event):
        print(self.tours[self.problemsList.GetCurrentSelection()])

    def uploadProblem(self,event):
        self.tours.append(self.addProblemInput.GetValue())
        self.problemsList.SetItems(self.tours)

app = wx.App()
TSP_GUI(None,"TSP_GUI").initialise()
app.MainLoop()
