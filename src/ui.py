import wx
from lib.queries import *
import matplotlib.pyplot as plt
from lib.db import Query
from lib.reader import READER

class PREFERENCES_DIALOG(wx.Dialog):
    def __init__(self,parent,reader):
        super(PREFERENCES_DIALOG,self).__init__(parent,title="Preferences",size=(450,200))
        panel = wx.Panel(self)
        self.reader = reader
        wx.StaticText(panel,label="TSP Directory Path",pos=(5,5)).SetFont(
            wx.Font(10,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL))

        self.path = wx.TextCtrl(panel,pos=(5,30),size=(300,-1),value=reader.getPath())
        self.confirm = wx.Button(panel, label="Submit",pos=(320,30))

        self.Bind(wx.EVT_BUTTON,self.editPath,self.confirm)
    
    def editPath(self,event):
        self.reader.setPath(self.path.GetValue())
        self.path.SetValue(self.reader.getPath())
        
class TSP_GUI(wx.Frame):
    def __init__(self,parent,title):
        super(TSP_GUI,self).__init__(parent,title=title,size=(1024,600))

        self.db = Query()
        self.reader = READER("F:\\1810ICT_SoftwareDevelopmentProcesses\\tsp_solver\\tsp_files\\")

        self._panel = wx.Panel(self,id=wx.ID_ANY,size=(600,400))
        self._menubar = wx.MenuBar()
        self._menu = wx.Menu()
        self._file_path = self._menu.Append(wx.ID_PREFERENCES)
        self._menubar.Append(self._menu,"File")
        self.SetMenuBar(self._menubar)

        self._font = wx.Font(12,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)

        self._uploadLabel = wx.StaticText(self._panel,label="Upload Problem",pos=(5,20)).SetFont(self._font)
        self._upload_problem_input = wx.TextCtrl(self._panel,pos=(5,50))
        self._upload_problem_submit = wx.Button(self._panel,label="Submit",pos=(125,50))

        self._problems_label = wx.StaticText(self._panel,label="Problems",pos=(5,100)).SetFont(self._font)
        self._problems_list_names = wx.ListBox(self._panel, pos=(5,125),size=(90,100),style=wx.LB_SINGLE)

        self._solution_label_times = wx.StaticText(self._panel,label="Solutions",pos=(125,100)).SetFont(self._font)
        self._solutions_list_times = wx.ListBox(self._panel,pos=(125,125),size=(100,100))

        self._loaded_label = wx.StaticText(self._panel,label="",pos=(5,250))
        self._loaded_label.SetFont(wx.Font(10,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL))
        self._load_button = wx.Button(self._panel,label="Load",pos=(125,250))

    def initialise(self):
        self.Show(True)    
        
class TSP_GUI_LOGIC(TSP_GUI):
    def __init__(self,parent,title):
        super(TSP_GUI_LOGIC,self).__init__(parent,title)
        self.setProblems()

        self.Bind(wx.EVT_BUTTON,self.uploadProblem,self._upload_problem_submit)
        self.Bind(wx.EVT_LISTBOX,self.selectProblem,self._problems_list_names)
        self.Bind(wx.EVT_LISTBOX,self.selectSolution,self._solutions_list_times)
        self.Bind(wx.EVT_MENU,self.editPath,self._file_path)

        self.initialise()

    def selectProblem(self,event):
        self._loaded_name = self._problems_list_names.GetString(self._problems_list_names.GetSelection())
        self._loaded_time = None
        self.setSolutionTimes(self._loaded_name)
        self._loaded_label.SetLabel(self._loaded_name)

    def setProblems(self):
        self._problems_list_names.Set(self.db.getProblems())
        
    def setSolutionTimes(self,name):
        self._solutions_list_times.Set(self.db.getSolutionTimes(name))

    def uploadProblem(self,event):
        problem = self._upload_problem_input.GetValue()
        a = self.reader.readIn(problem)
        size = a[0]["size"]
        comment = a[0]["comment"]
        nodes = a[1]
        
        self.db.addProblem(problem,size,comment)
        self.setProblems()

    def editPath(self,event):
        PREFERENCES_DIALOG(self,self.reader).Show()

    def selectSolution(self,event):
        self._loaded_time = int(self._solutions_list_times.GetString(self._solutions_list_times.GetSelection()))
        self._loaded_label.SetLabel(self._loaded_name + ", " + str(self._loaded_time) + " seconds")