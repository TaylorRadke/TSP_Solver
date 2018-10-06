import wx
from lib.queries import *
from lib.db import Query
from lib.reader import READER
from lib.solver import solve
from lib.plot import TSP_PLOT
from threading import Thread

from wx.lib.pubsub import pub as Publisher

class UploadThread(Thread):
    def __init__(self,tour,problem,attrs,gui):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.attrs = attrs
        self.gui = gui
        self.problem = problem
        self.db = Query()
        self.tour = tour
        self.start()    # start the thread
    #-------------- --------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
        self.db.addProblem(name = self.problem,size =  self.attrs["size"],comment = self.attrs["comment"])
        for node in self.tour:
                self.db.addCities(self.problem,node[0],node[1],node[2])
                wx.CallAfter(Publisher.sendMessage, "update",msg="")
        self.db.save()
        self.gui._problems_list_names.Set(self.db.getProblems())
        self.db.close()

class ProgressDialog(wx.Dialog):
    def __init__(self,range):
        """Constructor"""
        wx.Dialog.__init__(self, None, title="Upload Progress")
        self.count = 0
        self.range = range
        self.progress = wx.Gauge(self, range=self.range)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.progress, 0, wx.EXPAND)
        self.SetSizer(sizer)
 
        # create a pubsub listener
        Publisher.subscribe(self.updateProgress, "update")
 
    #----------------------------------------------------------------------
    def updateProgress(self, msg):
        """
        Update the progress bar
        """
        self.count += 1
        print(self.count,flush=True,end="\r")
        if self.count >= self.range:
            self.Destroy()
 
        self.progress.SetValue(self.count)

class PREFERENCES_DIALOG(wx.Dialog):
    def __init__(self,parent,reader):
        super(PREFERENCES_DIALOG,self).__init__(parent,title="Preferences",size=(450,200))
        panel = wx.Panel(self)
        self.reader = reader

        wx.StaticText(panel,label="TSP Directory Path",pos=(5,5)).SetFont(
            wx.Font(10,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL))

        self.path = wx.TextCtrl(panel,pos=(5,30),size=(300,-1),value=reader.getPath())
        self.confirm = wx.Button(panel, label="Browse",pos=(320,30))
        self.file = wx.DirDialog(self,defaultPath = self.reader.getPath())

        self.Bind(wx.EVT_BUTTON,self.editPath,self.confirm)
    
    def editPath(self,event):
        self.file.ShowModal()
        self.reader.setPath(self.file.GetPath())
        self.path.SetValue(self.reader.getPath())
        
class TSP_GUI(wx.Frame):
    def __init__(self,parent,title):
        super(TSP_GUI,self).__init__(parent,title=title,size=(600,600))

        self._framePanel = wx.Panel(self,size=(600,600),style=wx.EXPAND)
        self._uploadPanel = wx.Panel(self._framePanel)
        self._loadPanel = wx.Panel(self._framePanel)
        self._solvePanel = wx.Panel(self._framePanel)
        self._plotPanel = wx.Panel(self._framePanel)

        self.db = Query()
        self.reader = READER()
        self.plotter = TSP_PLOT(self._plotPanel)
        self.sizer = wx.GridBagSizer(5,0)
       
        self.SetSizer(self.sizer)

        self.sizer.Add(self._uploadPanel,pos=(0,0))
        self.sizer.Add(self._loadPanel,pos=(1,0),span=(1,1))
        self.sizer.Add(self._solvePanel,pos=(3,0))
        self.sizer.Add(self._plotPanel,pos=(0,1),span=(3,3))

        #Preferences Tab
        self._menubar = wx.MenuBar()
        self._menu = wx.Menu()
        self._file_path = self._menu.Append(wx.ID_PREFERENCES)
        self._menubar.Append(self._menu,"File")
        self.SetMenuBar(self._menubar)

        # Upload Options
        self._uploadLabel = wx.StaticText(self._uploadPanel,label="Upload Problem")
        self._upload_problem_input = wx.TextCtrl(self._uploadPanel)
        self._upload_problem_submit = wx.Button(self._uploadPanel,label="Submit")

        #Upload Sizer
        self.uploadSizer = wx.GridBagSizer(0,0)
        self.uploadSizer.Add(self._uploadLabel,pos=(0,0),span=(1,2))
        self.uploadSizer.Add(self._upload_problem_input,pos=(1,0),span=(1,2))
        self.uploadSizer.Add(self._upload_problem_submit,pos=(1,3))
        self._uploadPanel.SetSizer(self.uploadSizer)

        #Load Options
        self._problems_label = wx.StaticText(self._loadPanel,label="Problems")
        self._problems_list_names = wx.ListBox(self._loadPanel,style=wx.LB_SINGLE)
        self._solution_label_times = wx.StaticText(self._loadPanel,label="Solutions")
        self._solutions_list_times = wx.ListBox(self._loadPanel)
        self._loaded_label = wx.StaticText(self._loadPanel,label="")
        self._load_button = wx.Button(self._loadPanel,label="Load")

        #Load Sizer
        self.loadSizer = wx.GridBagSizer(0,10)
        self.loadSizer.Add(self._problems_label,pos=(0,0))
        self.loadSizer.Add(self._solution_label_times,pos=(0,1))
        self.loadSizer.Add(self._problems_list_names,pos=(1,0))
        self.loadSizer.Add(self._solutions_list_times,pos=(1,1))
        self.loadSizer.Add(self._loaded_label,pos=(3,0))
        self.loadSizer.Add(self._load_button,pos=(4,1))
        self._loadPanel.SetSizer(self.loadSizer)

        self._solve_problem = wx.StaticText(self._solvePanel)

        self._solve_time_label = wx.StaticText(self._solvePanel,label="Time")
        self._solve_input = wx.TextCtrl(self._solvePanel)
        self._solve_submit = wx.Button(self._solvePanel,label="Solve")
        self._save_solved_button = wx.Button(self._solvePanel,label="Save Solution")

        #Set Label Fonts
        self._font = wx.Font(12,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)

        self._uploadLabel.SetFont(self._font)
        self._problems_label.SetFont(self._font)
        self._solution_label_times.SetFont(self._font)
        self._solve_time_label.SetFont(self._font)
        self._loaded_label.SetFont(wx.Font(11,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL))
        self._solve_problem.SetFont(wx.Font(11,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL))

        #Hide widgets
        
        self._solve_time_label.Hide()
        self._solve_input.Hide()
        self._solve_submit.Hide()
        self._save_solved_button.Hide()



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
        self.Bind(wx.EVT_BUTTON,self.loadSelected,self._load_button)
        self.Bind(wx.EVT_BUTTON, self.solveLoaded, self._solve_submit)
        self.Bind(wx.EVT_BUTTON,self.saveSolved,self._save_solved_button)

        self.initialise()

    def selectProblem(self,event):
        self._loaded_name = self._problems_list_names.GetString(self._problems_list_names.GetSelection())
        self._loaded_time = None
        self.setSolutionTimes(self._loaded_name)
        self._loaded_label.SetLabel(self._loaded_name)

        self._loaded_label.Show()
        self._load_button.Show()

    def setProblems(self):
        self._problems_list_names.Set(self.db.getProblems())
        
    def setSolutionTimes(self,name):
        self._solutions_list_times.Set(self.db.getSolutionTimes(name))

    def uploadProblem(self,event):
        problem = self._upload_problem_input.GetValue()
        a = self.reader.readIn(problem)
        if (a is not None):
            self.size = a[0]["size"]
            
            UploadThread(a[1],problem,a[0],self)
            ProgressDialog(self.size).ShowModal()
            self.setProblems()


    def editPath(self,event):
        PREFERENCES_DIALOG(self,self.reader).Show()

    def selectSolution(self,event):
        self._loaded_time = int(self._solutions_list_times.GetString(self._solutions_list_times.GetSelection()))
        self._loaded_label.SetLabel(self._loaded_name + ", " + str(self._loaded_time) + " secs")
        
        self._load_button.Show()
        self._loaded_label.Show()

    def loadSelected(self,event):

        if (self._loaded_name and not self._loaded_time):

            self._loaded_tour = self.db.getCities(self._loaded_name)
            self._solve_problem.SetLabel(self._loaded_name)
    
            self.plotter.updatePlot(self.getx(self._loaded_tour),self.gety(self._loaded_tour))

        elif (self._loaded_name and self._loaded_time):

            #load solution
            a = self.db.getSolutionCities(self._loaded_name,int(self._loaded_time))
            b = self.db.getCities(self._loaded_name)
            c = []

            for i in a:
                for j in range(len(b)):
                    if i == b[j][0]:
                        c.append(b[j])

            self._loaded_tour = c
            self.plotter.updatePlot(self.getx(self._loaded_tour),self.gety(self._loaded_tour))
            self._solve_problem.SetLabel(self._loaded_name + ", " + str(self._loaded_time) + " secs")

        self._load_button.Hide()
        self._loaded_label.Hide()
            
        self._solve_input.Show()
        self._solve_submit.Show()
        self._solve_time_label.Show()
    
    def getx(self,tour):
        a = [a[1] for a in tour]
        a.append(a[0])
        return a

    def gety(self,tour):
        a = [a[2] for a in tour]
        a.append(a[0])
        return a

    def solveLoaded(self,event):
        if self._loaded_tour:
            self._solve_submit.Hide()
            self._solve_time = int(self._solve_input.GetValue())
            a = solve(self._loaded_tour,self._solve_time)
            self._solution_tour_length = a[0]
            self._solution_tour_str = a[1]
            self._solution_tour = a[2]
            self.plotter.updatePlot(self.getx(self._solution_tour),self.gety(self._solution_tour))
            self._save_solved_button.Show()
            self._solve_submit.Show()
            

    def saveSolved(self,event):
        if self._solution_tour:
            self.db.addSolution(self._loaded_name,self._solution_tour_length,self._solve_time,self._solution_tour_str)
            self.db.save()
            self.setSolutionTimes(self._loaded_name)