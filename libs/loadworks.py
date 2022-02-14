from libs import globals as g

def load(url):
	work = g.AO3.Work(g.AO3.utils.workid_from_url(url))
	worktext=''
	workstats=f'title:\t{work.title}\nAuthors:\t{work.authors}\nChapters:\t{work.nchapters}\nWords:\t{work.words}\nHits:\t{work.hits}\nKudos:\t{work.kudos}\nBookmarks:\t{work.bookmarks}\n'
	worktags=work.tags
	workfandoms=work.fandoms
	pnl=g.wx.Panel(g.frame)
	sizer=g.wx.BoxSizer()
	stats=g.wx.textCtrl(pnl,style=g.wx.TE_MULTILINE|g.wx.TE_READONLY,
	stats.SetValue(workstats)
	sizer.Add(window=stats,0)
	pnl.setSizerAndFit(sizer)
	)