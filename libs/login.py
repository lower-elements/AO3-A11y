from . import globals as g
#this is where the functions for logging into AO3 are stored. We will call these from the main function in libs/main.py. 

def login():
	try:
		try:
			with open('./configfiles/user.usr','r') as f:
				user=f.read()
			password=g.keyring.get_password('AO3',user)
			g.session = g.AO3.Session(user,password)
		except:
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
			g.keyring.set_password('AO3', login['user'], login['password'])
			with open('user.usr','w') as f:
				f.write(login['user'])			
			g.session = g.AO3.Session(login['user'],login['password'])
		
	except:
		g.wx.MessageBox('Please try again and try checking if your username and password are correct', 'Warning', g.wx.OK | g.wx.ICON_WARNING)
		g.frame.On_Quit()
		