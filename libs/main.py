from . import globals as g
#the file where the bulk of the action occurs
app=g.wx.App()
APP_EXIT=1
APP_LOGOUT=2
APP_LOGIN=3
class frame(g.wx.Frame):
	def __init__(self, *args, **kwargs):
		super(frame, self).__init__(*args, **kwargs)
		self.setup()
	
	def setup(self):
		toolbar=g.wx.MenuBar()
		filemenu=g.wx.Menu()
		usermenu=g.wx.Menu()
		quitoption=g.wx.MenuItem(filemenu, APP_EXIT, '&Quit')
		filemenu.Append(quitoption)
		login=g.wx.MenuItem(usermenu, APP_LOGIN, '&log in')
		logout=g.wx.MenuItem(usermenu, APP_LOGOUT, '&log out')
		usermenu.Append(logout)
		usermenu.Append(login)
		self.Bind(g.wx.EVT_MENU, self.On_Quit, id=APP_EXIT)
		self.Bind(g.wx.EVT_MENU, self.On_Logout, id=APP_LOGOUT)
		self.Bind(g.wx.EVT_MENU, self.On_Login, id=APP_LOGIN)
		toolbar.Append(filemenu, '&File')
		toolbar.Append(usermenu, '&user')
		self.SetMenuBar(toolbar)
		
		
		self.SetTitle("AO3 A11y. Development build")
		self.Centre()
		self.Show()
		with open('configfiles/user.usr','r+') as f:
			user = f.read()
		if user=='':
			dlg=g.wx.MessageDialog(None, 'Would you like to log in. Logging in allows for greater abilities such as leaving kudos.','Log in?', g.wx.YES_NO | g.wx.ICON_QUESTION)
			if dlg.ShowModal()==g.wx.ID_YES:
				g.login.login()
			else:
				g.settings['account']=False
			
		
	
	def On_Quit(self, e):
		g.savestate()
		self.Close()
	
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
	
	def On_Login(self,e):
		g.login.login()

def main():
	g.frame=frame(None)
	app.MainLoop()