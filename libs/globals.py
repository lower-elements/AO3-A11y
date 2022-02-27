import AO3
import json
import keyring
import wx
import os

from libs import login
from libs import main
from libs import loadworks
from libs import library as l

if not os.path.exists('configfiles/'):
    os.mkdir('configfiles/')
if not os.path.exists('configfiles/settings.json'):
    with open('configfiles/settings.json','w+') as f:
        f.write('{}')
    
if not os.path.exists('configfiles/bookmarks.json'):
    with open('configfiles/bookmarks.json','w+') as f:
        f.write('{}')
if not os.path.exists('configfiles/librarysaves.json'):
    with open('configfiles/librarysaves.json','w+') as f:
        f.write('{}')
if not os.path.exists('configfiles/librarydownloads.json'):
    with open('configfiles/librarydownloads.json','w+') as f:
        f.write('{}')
if not os.path.exists('configfiles/user.usr'):
    with open('configfiles/user.usr','w+') as f:
        f.write('')

frame=None #this is a variable available to the entire program that stores the wx.frame object which is the main window
session=None #this is a variable available also to the entire program which stores the AO3 api session. 

settings=json.loads(open('configfiles/settings.json','r').read()) #this opens the settings.json file in the form of a python dictionary. 
bookmarks=json.loads(open('configfiles/bookmarks.json','r').read())
librarysaves=json.loads(open('configfiles/librarysaves.json','r').read())
librarydownloads=json.loads(open('configfiles/librarydownloads.json','r').read())

notebook=None
librry=None
version="V2022.02.27-Alpha"

#this is a function which can be used to save the settings of the program by sending the settings dictionary back to the settings.json file. We're currently only using this just before closing the program but in the future we could add a separate thread that runs it periodically, like an autosave. 
def savestate():
    with open('configfiles/settings.json','w') as f:
        json.dump(settings, f)
    with open('configfiles/bookmarks.json','w') as f:
        json.dump(bookmarks,f)    
    with open('configfiles/librarysaves.json','w') as f:
        json.dump(librarysaves,f)
    with open('configfiles/librarydownloads.json','w') as f:
        json.dump(librarydownloads,f)
