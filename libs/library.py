from libs import globals as g

class library():
    def __init__(self):
        g.library=g.wx.Panel(g.notebook)
        g.notebook.AddPage(g.library,'library')
        self.sizer=g.wx.BoxSizer()
        self.savedlabel=g.wx.StaticText(g.library,label='select  saved work.')
        saves=[]
        for i in g.librarysaves:
            saves.append(i)
        
        self.saved=g.wx.ComboBox(g.library,choices=saves,style=g.wx.CB_DROPDOWN|g.wx.CB_READONLY)
        self.load1=g.wx.Button(g.library,label='load work')
        self.load1.Bind(g.wx.EVT_BUTTON,self.On_Load1)
        self.remove1=g.wx.Button(g.library,label='remove work')
        self.remove1.Bind(g.wx.EVT_BUTTON,self.On_Remove1)
        self.sizer.Add(self.savedlabel,0)
        self.sizer.Add(self.saved,0)
        self.sizer.Add(self.load1,0)
        self.sizer.Add(self.remove1,0)

        self.downloadedlabel=g.wx.StaticText(g.library,label='select  downloded work.')
        downloads=[]
        for i in g.librarydownloads:
            downloads.append(i)
        
        self.downloded=g.wx.ComboBox(g.library,choices=downloads,style=g.wx.CB_DROPDOWN|g.wx.CB_READONLY)
        self.load2=g.wx.Button(g.library,label='load work')
        self.load2.Bind(g.wx.EVT_BUTTON,self.On_Load2)
        self.remove2=g.wx.Button(g.library,label='remove work')
        self.remove2.Bind(g.wx.EVT_BUTTON,self.On_Remove2)
        self.sizer.Add(self.downloadedlabel,0)
        self.sizer.Add(self.downloded,0)
        self.sizer.Add(self.load2,0)
        self.sizer.Add(self.remove2,0)
        g.library.SetSizerAndFit(self.sizer)

    
    def On_Load1(self,event):
        value=self.saved.GetValue()
        g.loadworks.work(g.librarysaves[value])

    def On_Load2(self,event):
        value=self.downloded.GetValue()
        g.loadworks.work(g.librarydownloads[value])

    def On_Remove1(self,event):
        value=self.saved.GetValue()
        g.librarysaves.pop(value)
        self.refresh()
    def On_Remove2(self,event):
        value=self.downloded.GetValue()
        g.librarydownloads.pop(value)
        self.refresh()
    def refresh(self):
        saves=[]
        for i in g.librarysaves:
            saves.append(i)
        self.saved.choices=saves
        downloads=[]
        for i in g.librarydownloads:
            downloads.append(i)
        self.downloded.choices=downloads
