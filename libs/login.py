from . import globals as g
#this is where the functions for logging into AO3 are stored. We will call these from the main function in libs/main.py. 

#the function for logging into AO3
def login():
	with open("configfiles/user.usr","r+") as f: #this loads the user.usr file for access to see if a username is available. 
		user = f.read()
	try:
		#now we check to see if user.usr contains a username, if not we'll log in by requesting for username an password. Otherwise we access the keyring service. 
		if user != "": 
			password=g.keyring.get_password('AO3',user) #accesses keyring to retreave credentials. 
			g.session = g.AO3.Session(user,password) #quite obviously logs in. 
		
		else:
			login_dict={"user":"","password":""} # a dictionary to store username and password
			dlg=g.wx.TextEntryDialog(g.frame, 'Please enter your Archive of Our Own username so you can browse AO3.','login') #create the text entry dialog for the username with a parent of g.frame which is the main window. 
			dlg.SetValue("") #sets the value of the username field to be nothing. 
			if dlg.ShowModal() == g.wx.ID_OK: 
				login_dict['user']=dlg.GetValue() #if the dialog returns OK, retreaves the user input and sets the dictionary key user to that. 
			dlg.Destroy() #we no longer need the dialog so say goodbye. 
			#now we have the same for password
			dlg=g.wx.TextEntryDialog(g.frame, 'Please enter your Archive of Our Own password so you can browse AO3.','login')
			dlg.SetValue("")
			if dlg.ShowModal() == g.wx.ID_OK:
				login_dict['password']=dlg.GetValue()
			dlg.Destroy()
			g.keyring.set_password('AO3', login_dict['user'], login_dict['password']) #sets the keyring service for AO3. 
			with open('configfiles/user.usr','w+') as f:
				f.write(login_dict['user']) #writes the username to user.usr so the program can access it next time it opens. 
			g.session = g.AO3.Session(login_dict['user'],login_dict['password']) #again, creates the AO3 session. 
			g.wx.MessageBox('You have just logged in as: '+login_dict['user'],'logged in', g.wx.OK) #a dialog box that is a confirmation of a successful login.
			g.settings['account']=True #sets the account variable in settings to true. We can use this to prevent errors from crashing the program if not logged in users attempt to do something they are unable to do due to AO3 limitations.
		
	except:
		#if an error occurs while logging in, show a warning, save the settings then close the program. 
		g.wx.MessageBox('Please try again and try checking if your username and password are correct', 'Warning', g.wx.OK | g.wx.ICON_WARNING)
		g.savestate()
		g.frame.Close()