from . import globals as g
#the file where the bulk of the action occurs

app=g.wx.App() #this is required to start the MainLoop which registers events that are required to make the program work. 
#the following are IDs for different occurences. E.G. APP_EXIT is the code given to exiting the program. 
APP_EXIT=1
APP_LOGOUT=2
APP_LOGIN=3

#next we create a frame class that inherits from wxpython's frame class
class frame(g.wx.Frame):
	def __init__(self, *args, **kwargs):
		super(frame, self).__init__(*args, **kwargs)
		self.setup()
	
	#this functions is what sets up the window
	def setup(self):
		toolbar=g.wx.MenuBar() #iniciates the menu bar
		filemenu=g.wx.Menu() #creates the 'file' submenu
		usermenu=g.wx.Menu() #makes the 'user' sub menu
		quitoption=g.wx.MenuItem(filemenu, APP_EXIT, '&Quit') #makes the quit option. Its parent is the file menu and it returns the APP_EXIT id and has the display name. 
		filemenu.Append(quitoption) #obviously adds the quit option to the file menu
		login=g.wx.MenuItem(usermenu, APP_LOGIN, '&log in') #creates the log in option. 
		logout=g.wx.MenuItem(usermenu, APP_LOGOUT, '&log out') #creates log out option
		#adds log in and log out to user menu
		usermenu.Append(logout)
		usermenu.Append(login)
		#next we bind a function to the codes defined at the top of the file. 
		self.Bind(g.wx.EVT_MENU, self.On_Quit, id=APP_EXIT)
		self.Bind(g.wx.EVT_MENU, self.On_Logout, id=APP_LOGOUT)
		self.Bind(g.wx.EVT_MENU, self.On_Login, id=APP_LOGIN)
		#adds the menus to the menu bar itself. 
		toolbar.Append(filemenu, '&File')
		toolbar.Append(usermenu, '&user')
		self.SetMenuBar(toolbar)
		
		#sets title and centres the window on the screen. Then makes the window show. 
		self.SetTitle("AO3 A11y. Development build")
		self.Centre()
		self.Show()
		#next we check if there is a username in user.usr. If not we ask if the user wants to log in. If not we go on without an account. 
		with open('configfiles/user.usr','r+') as f:
			user = f.read()
		if user=='':
			dlg=g.wx.MessageDialog(None, 'Would you like to log in. Logging in allows for greater abilities such as leaving kudos.','Log in?', g.wx.YES_NO | g.wx.ICON_QUESTION) #creates teh yes or no dialog. 
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
	
	#the functions that runs when APP_LOGIN is enacted. 
	def On_Login(self,e):
		g.login.login()
	
	def On_URL(self,e):
		dlg=g.wx.Message_Box('Enter the url to the archive of oyr own work which you wish to open'
		self.pnl = g.wx.Panel(self)
		vbox = g.wx.BoxSizer(g.wx.VERTICAL)


#the function that creates the frame class and starts the MainLoop
def main():
	g.frame=frame(None)
	app.MainLoop()