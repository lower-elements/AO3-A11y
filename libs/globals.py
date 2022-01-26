import AO3
import wx
import cryptography
from libs import login
from libs import main

app=wx.App()
APP_EXIT=1

class frame(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(frame, self).__init__(*args, **kwargs)
		self.setup()
	
	def setup(self):
		toolbar=wx.MenuBar()
		filemenu=wx.Menu()
		quitoption=wx.MenuItem(filemenu, APP_EXIT, '&Quit')
		filemenu.Append(quitoption)
		self.Bind(wx.EVT_MENU, self.On_Quit, id=APP_EXIT)
		toolbar.Append(filemenu, '&File')
		self.SetMenuBar(toolbar)
		
		self.SetTitle("AO3 A11y. Development build")
		self.Centre()
	
	def On_Quit(self, e):
		self.Close()
	
