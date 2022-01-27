import AO3
import json
import keyring
import wx
from libs import login
from libs import main

frame=None
settings=json.loads(open('configfiles/settings.json','r').read())

def savestate():
	with open('configfiles/settings.json','w') as f:
		json.dump(settings, f)
	
