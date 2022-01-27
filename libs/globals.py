import AO3
import json
import keyring
import wx
from libs import login
from libs import main

frame=None #this is a variable available to the entire program that stores the wx.frame object which is the main window
session=None #this is a variable available to the also to the entire program which stores the AO3 api session. 
settings=json.loads(open('configfiles/settings.json','r').read()) #this opens the settings.json files in the form of a python dictionary. 

#this is a function which can be used to save the settings of the program by sending the settings dictionary back to the settings.json file. I'm currently only using this just before closing the program but in futre we could add a separate thread that runs it periodically, like an autosave. 
def savestate():
	with open('configfiles/settings.json','w') as f:
		json.dump(settings, f)
	
