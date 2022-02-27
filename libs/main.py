from cProfile import label
from click import style
from . import globals as g
#the file where the bulk of the action occurs

app=g.wx.App() #this is required to start the MainLoop which registers events that are required to make the program work. 
#the following are IDs for different occurences. E.G. APP_EXIT is the code given to exiting the program. 
APP_EXIT=1
APP_LOGOUT=2
APP_LOGIN=3
APP_LOAD=4

#next we create a frame class that inherits from wxpython's frame class
class frame(g.wx.Frame):
    def __init__(self, *args, **kwargs):
        super(frame, self).__init__(*args, **kwargs)
        self.setup()
    
    #this function is what sets up the window
    def setup(self):
        toolbar=g.wx.MenuBar() #iniciates the menu bar
        filemenu=g.wx.Menu()
        worksmenu=g.wx.Menu()
        usermenu=g.wx.Menu()
        quitoption=g.wx.MenuItem(filemenu, APP_EXIT, '&Quit... ') #makes the quit option. Its parent is the file menu and it returns the APP_EXIT id and has the display name. 
        filemenu.Append(quitoption)
        login=g.wx.MenuItem(usermenu, APP_LOGIN, '&Log in... ') #creates the log in option. 
        logout=g.wx.MenuItem(usermenu, APP_LOGOUT, '&Log out... ')
        usermenu.Append(login)
        usermenu.Append(logout)
        Load_URL_Option=g.wx.MenuItem(worksmenu, APP_LOAD, '&Load a work from an URL...')
        worksmenu.Append(Load_URL_Option)
        #next we bind a function to the codes defined at the top of the file. 
        self.Bind(g.wx.EVT_MENU, self.On_Quit, id=APP_EXIT)
        self.Bind(g.wx.EVT_MENU, self.On_Logout, id=APP_LOGOUT)
        self.Bind(g.wx.EVT_MENU, self.On_URL, id=APP_LOAD)
        self.Bind(g.wx.EVT_MENU, self.On_Login, id=APP_LOGIN)
        #adds the menus to the menu bar itself. 
        toolbar.Append(filemenu, '&File')
        toolbar.Append(usermenu, '&User')
        toolbar.Append(worksmenu, '&Works')
        self.SetMenuBar(toolbar)
        
        #add a panel 
        pnl = g.wx.Panel(self)
        #add a notebook with the tabs on top
        g.notebook = g.wx.Notebook(pnl)
        #Panel for the home tabb.
        self.home = g.wx.Panel(g.notebook)
        g.notebook.AddPage(self.home, 'Home')
        self.sizer=g.wx.BoxSizer()
        #here are text fields for version and license which will go at the bottom of the home tab, if you want to add something to the home page, add it above this comment. 
        self.versionlabel=g.wx.StaticText(self.home,label="version")
        self.versiontext=g.wx.TextCtrl(self.home,style=g.wx.TE_MULTILINE|g.wx.TE_DONTWRAP|g.wx.TE_READONLY)
        self.versiontext.SetValue(g.version)
        self.sizer.Add(self.versionlabel,0)
        self.sizer.Add(self.versiontext)
        self.licenselabel=g.wx.StaticText(self.home,label="license")
        self.licensetext=g.wx.TextCtrl(self.home,style=g.wx.TE_READONLY|g.wx.TE_MULTILINE|g.wx.TE_DONTWRAP|g.wx.TE_AUTO_URL)
        with open("LICENSE","r") as f:
            self.licensetext.SetValue("The Archive Of Our Own Accessibility project (AO3-A11y) is released under the GNU General Public License V3.\nThe source code to this project can be found at \nhttps://github.com/ao3-a11y/ao3-a11y\n\nLicense: \n"+f.read())
        self.sizer.Add(self.licenselabel,0)
        self.sizer.Add(self.licensetext)
        
        g.l.library()
        
        #sets title and centres the window on the screen. Then makes the window show. 
        self.SetTitle("AO3 A11y")
        self.Centre()
        self.Show()
        #next we check if there is a username in user.usr. If not we ask if the user wants to log in. If not we go on without an account. 
        with open('configfiles/user.usr','r+') as f:
            user = f.read()
        if user=='':
            dlg=g.wx.MessageDialog(None, 'Would you like to log in. Logging in allows for greater abilities such as leaving kudos.','Log in?', g.wx.YES_NO | g.wx.ICON_QUESTION)
            if dlg.ShowModal()==g.wx.ID_YES: 
                g.login.login()
            else:
                g.settings['account']=False
            
        
    
    
    #the function that runs when APP_EXIT is enacted, saves settings then closes the program. 
    def On_Quit(self, e):
        g.savestate()
        self.Close()
    
    #the function that runs when APP_LOGOUT is enacted. 
    def On_Logout(self,e):
        with open('configfiles/user.usr','r+') as f:
            user=f.read()
        with open('configfiles/user.usr','w+') as f:
            f.write('')
        g.keyring.delete_password('AO3', user)
        g.session=None
        g.wx.MessageBox('You have just logged out from the account: '+user,'logged out', g.wx.OK)
        g.settings['account']=False
        g.savestate()
    
    #the function that runs when APP_LOGIN is enacted. 
    def On_Login(self,e):
        g.login.login()
    
    def On_URL(self,e):
        dlg=g.wx.TextEntryDialog(g.frame, 'Enter the URL to the AO3 work which you wish to open...','load work')
        dlg.SetValue('')
        if dlg.ShowModal() == g.wx.ID_OK:
            g.loadworks.work(dlg.GetValue())
        dlg.Destroy()

    def On_Closeup(self,event):
        book=self.saved.GetValue()
        link=g.librarysaves[book]
        g.loadworks(link)
    
#the function that creates the frame class and starts the MainLoop
def main():
    g.frame=frame(None)
    app.MainLoop()