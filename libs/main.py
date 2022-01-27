from . import globals as g
#the file where the bulk of the action occurs
app=g.wx.App()
APP_EXIT=1
APP_LOGOUT=2

class frame(g.wx.Frame):
	def __init__(self, *args, **kwargs):
		super(frame, self).__init__(*args, **kwargs)
		self.setup()
	
	def setup(self):
		toolbar=g.wx.MenuBar()
		filemenu=g.wx.Menu()
		quitoption=g.wx.MenuItem(filemenu, APP_EXIT, '&Quit')
		logout=g.wx.MenuItem(filemenu, APP_LOGOUT, '&log out')
		filemenu.Append(quitoption)
		filemenu.Append(logout)
		self.Bind(g.wx.EVT_MENU, self.On_Quit, id=APP_EXIT)
		self.Bind(g.wx.EVT_MENU, self.On_Logout, id=APP_LOGOUT)
		toolbar.Append(filemenu, '&File')
		self.SetMenuBar(toolbar)
		
		
		self.SetTitle("AO3 A11y. Development build")
		self.Centre()
		self.Show()
		g.login.login()
		
	def On_Quit(self, e):
		self.Close()
	
	def On_Logout(self,e):
		with open('configfiles/user.usr','r+') as f:
			user=f.read()
		with open('configfiles/user.usr','w+') as f:
			f.write('')
		g.keyring.delete_password('AO3', user)
		g.session=None
		g.wx.MessageBox('You have just logged out from the account: '+user,'logged out', g.wx.OK)
		self.Close()

def main():
	g.frame=frame(None)
	app.MainLoop()