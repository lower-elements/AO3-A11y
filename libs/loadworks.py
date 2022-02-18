from libs import globals as g

class work():
    def __init__(self,URL):
        self.work, self.workfandoms,self.worktags, self.workstats=self.load(URL)
        self.book=g.wx.Panel(g.notebook)
        g.notebook.AddPage(self.book, self.work.title)
        self.sizer=g.wx.BoxSizer()
        self.titlelabel=g.wx.StaticText(self.book,label='title')
        self.title=g.wx.TextCtrl(self.book,style=g.wx.TE_MULTILINE|g.wx.TE_DONTWRAP|g.wx.TE_READONLY)
        self.title.SetValue(self.work.title)
        self.sizer.Add(self.titlelabel,0)
        self.sizer.Add(self.title)
        self.summerylabel=g.wx.StaticText(self.book,label='summery')
        self.summery=g.wx.TextCtrl(self.book,style=g.wx.TE_MULTILINE|g.wx.TE_READONLY|g.wx.TE_DONTWRAP)
        self.summery.SetValue(self.work.summary)
        self.sizer.Add(self.summerylabel,0)
        self.sizer.Add(self.summery)
        self.statslabel=g.wx.StaticText(self.book,label='book stats')
        self.stats=g.wx.TextCtrl(self.book,style=g.wx.TE_MULTILINE|g.wx.TE_READONLY|g.wx.TE_DONTWRAP)
        self.stats.SetValue(self.workstats)
        self.sizer.Add(self.statslabel,0)
        self.sizer.Add(self.stats,0)
        self.tagslabel=g.wx.StaticText(self.book,label='book tags')
        self.tags=g.wx.TextCtrl(self.book,style=g.wx.TE_MULTILINE|g.wx.TE_READONLY|g.wx.TE_DONTWRAP)
        self.tags.SetValue(self.worktags)
        self.sizer.Add(self.tagslabel,0)
        self.sizer.Add(self.tags,0)
        self.fandomslabel=g.wx.StaticText(self.book,label='book fandoms')
        self.fandoms=g.wx.TextCtrl(self.book,style=g.wx.TE_MULTILINE|g.wx.TE_READONLY|g.wx.TE_DONTWRAP)
        self.fandoms.SetValue(self.workfandoms)
        self.sizer.Add(self.fandomslabel,0)
        self.sizer.Add(self.fandoms,0)
        self.ework=g.wx.CheckBox(self.book,label='Chapter by chapter')
        self.ework.Bind(g.wx.EVT_CHECKBOX, self.On_Toggle)
        self.sizer.Add(self.ework,0)
        self.worktextlabel=g.wx.StaticText(self.book,label='worktext')
        self.worktext=g.wx.TextCtrl(self.book,style=g.wx.TE_DONTWRAP|g.wx.TE_READONLY|g.wx.TE_MULTILINE)
        self.text=''
        for index, i in enumerate(self.work.chapters):
            self.text=self.text+'\tChapter '+str(index+1)+': '+i.title+'\n'+i.text+'\n\n'
        self.worktext.SetValue(self.text)
        self.chapterslabel=g.wx.StaticText(self.book,label='Select a chapter')
        self.choicelist=[]
        for index, i in enumerate(self.work.chapters):
            self.choicelist.append('chapter '+str(index+1)+': '+i.title)
        self.chapters=g.wx.Choice(self.book,choices=self.choicelist)
        self.chapters.Bind(g.wx.EVT_CHOICE, self.on_change)
        self.chapters.SetSelection(0)
        self.sizer.Add(self.chapterslabel,0)
        self.sizer.Add(self.chapters,0)
        self.chapters.Hide()
        self.sizer.Add(self.worktextlabel,0)
        self.sizer.Add(self.worktext,0)
        self.Close_Work=g.wx.Button(self.book,label='Close work')
        self.Close_Work.Bind(g.wx.EVT_BUTTON,self.On_Shut)
        self.sizer.Add(self.Close_Work,0)
        self.book.SetSizerAndFit(self.sizer)
    
    def On_Shut(self,event):
        g.notebook.RemovePage(g.notebook.GetSelection())
        del self
    
    def on_change(self,event):
        self.text='chapter '+str(self.chapters.GetSelection()+1)+': '+self.work.chapters[self.chapters.GetSelection()].title+'\n'+self.work.chapters[self.chapters.GetSelection()].text
        self.worktext.SetValue(self.text)
    
    def On_Toggle(self, event):
        ework=event.GetEventObject()
        ework.SetLabel('Chapter by chapter')
        if ework.IsChecked():
            self.chapters.Show()
            self.text='chapter '+str(self.chapters.GetSelection()+1)+': '+self.work.chapters[self.chapters.GetSelection()].title+'\n'+self.work.chapters[self.chapters.GetSelection()].text
            self.worktext.SetValue(self.text)
            
        else:
            self.chapters.Hide()
            self.text=''
            for index, i in enumerate(self.work.chapters):
                self.text=self.text+'\tChapter '+str(index+1)+': '+i.title+'\n'+i.text+'\n\n'
            self.worktext.SetValue(self.text)
        
    
    
    def load(self,URL):
        work = g.AO3.Work(g.AO3.utils.workid_from_url(URL))
        workstats=f'Authors: {work.authors}\nChapters: {work.nchapters}\nWords: {work.words}\nHits: {work.hits}\nKudos: {work.kudos}\nBookmarks: {work.bookmarks}'
        worktags=''
        for i in work.tags:
            worktags=worktags+i+'\n'
        if worktags=='':
            worktags='no tags available'
        workfandoms=''
        for i in work.fandoms:
            workfandoms=workfandoms+i+'\n'
        if workfandoms=='':
            workfandoms='no fandoms available for this work'
        return work, workfandoms, worktags, workstats
    