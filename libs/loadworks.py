from libs import globals as g

def loadwork(url):
	work = g.AO3.Work(g.AO3.utils.workid_from_url(url))
	worktext={}
	
	