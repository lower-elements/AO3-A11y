from .globals import *
#this is where the functions for logging into AO3 are stored. We will call these from the main function in libs/main.py. 

def login():
	login={"user":"","password":""}
	dlg=wx.TextEntryDialog(frame, 'So you can brouse Archive of Our Own, please enter your AO3 username. ','login')
	dlg.SetValue("")
	if dlg.ShowModal() == wx.ID_OK:
		login['user']=dlg.GetValue()
	dlg.Destroy()
	
