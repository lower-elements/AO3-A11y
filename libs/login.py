from . import globals as g
#this is where the functions for logging into AO3 are stored. We will call these from the main function in libs/main.py. 

def login():
	with open("configfiles/user.usr","r+") as f:
		user = f.read()
	try:
		#now we check to see if user.usr contains a username, if not we'll log in by requesting for username an password. Otherwise we access the keyring service. 
		if user != "": 
			password=g.keyring.get_password('AO3',user) #accesses keyring to retreeve credentials. 
			g.session = g.AO3.Session(user,password)
		
		else:
			login_dict={"user":"","password":""}
			dlg=g.wx.TextEntryDialog(g.frame, 'Please enter your Archive of Our Own username so you can browse AO3.','login')
			dlg.SetValue("")
			if dlg.ShowModal() == g.wx.ID_OK: 
				login_dict['user']=dlg.GetValue()
			dlg.Destroy()
			#now we have the same for password
			dlg=g.wx.TextEntryDialog(g.frame, 'Please enter your Archive of Our Own password so you can browse AO3.','login')
			dlg.SetValue("")
			if dlg.ShowModal() == g.wx.ID_OK:
				login_dict['password']=dlg.GetValue()
			dlg.Destroy()
			g.keyring.set_password('AO3', login_dict['user'], login_dict['password']) #sets the keyring service for AO3. 
			with open('configfiles/user.usr','w+') as f:
				f.write(login_dict['user'])
			g.session = g.AO3.Session(login_dict['user'],login_dict['password'])
			g.wx.MessageBox('You have just logged in as: '+login_dict['user'],'logged in', g.wx.OK)
			g.settings['account']=True
		
	except:
		#if an error occurs while logging in, show a warning, save the settings then close the program. 
		g.wx.MessageBox('Please try again and try checking if your username and password are correct', 'Warning', g.wx.OK | g.wx.ICON_WARNING)
		g.savestate()
		g.frame.Close()