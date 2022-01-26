from . import globals as g
#this is where the functions for logging into AO3 are stored. We will call these from the main function in libs/main.py. 

def login():
	login={"user":"","password":""}
	dlg=g.wx.TextEntryDialog(g.frame, 'Please enter your Archive of Our Own username so you can browse AO3.','login')
	dlg.SetValue("")
	if dlg.ShowModal() == g.wx.ID_OK:
		login['user']=dlg.GetValue()
	dlg.Destroy()
	dlg=g.wx.TextEntryDialog(g.frame, 'Please enter your Archive of Our Own password so you can browse AO3.','login')
	dlg.SetValue("")
	if dlg.ShowModal() == g.wx.ID_OK:
		login['password']=dlg.GetValue()
	dlg.Destroy()

