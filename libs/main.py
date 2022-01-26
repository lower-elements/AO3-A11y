from . import globals as g
#the file where the bulk of the action occurs
app=g.wx.App()
APP_EXIT=1

class frame(g.wx.Frame):
	def __init__(self, *args, **kwargs):
		super(frame, self).__init__(*args, **kwargs)
		self.setup()
	
	def setup(self):
		toolbar=g.wx.MenuBar()
		filemenu=g.wx.Menu()
		quitoption=g.wx.MenuItem(filemenu, APP_EXIT, '&Quit')
		filemenu.Append(quitoption)
		self.Bind(g.wx.EVT_MENU, self.On_Quit, id=APP_EXIT)
		toolbar.Append(filemenu, '&File')
		self.SetMenuBar(toolbar)
		
		
		self.SetTitle("AO3 A11y. Development build")
		self.Centre()
		self.Show()
		g.login.login()
		
	def On_Quit(self, e):
		self.Close()
	
def main():
	g.frame=frame(None)
	app.MainLoop()