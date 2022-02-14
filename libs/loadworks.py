from libs import globals as g

def load(url):
	work = g.AO3.Work(g.AO3.utils.workid_from_url(url))
	worktext=''
	workstats=f'title: {work.title}\nAuthors: {work.authors}\nChapters: {work.nchapters}\nWords: {work.words}\nHits: {work.hits}\nKudos: {work.kudos}\nBookmarks: {work.bookmarks}\n'
	worktags=''
	for i in work.tags:
		worktags += i + '\n'
	workfandoms=work.fandoms
	book=g.wx.Panel(g.notebook)
	g.notebook.AddPage(book, work.title)
	sizer=g.wx.BoxSizer()
	statslabel=g.wx.StaticText(book,label='book stats')
	stats=g.wx.TextCtrl(book,style=g.wx.TE_MULTILINE|g.wx.TE_READONLY)
	stats.SetValue(workstats)
	sizer.Add(statslabel,0)
	sizer.Add(stats,0)
	tagslabel=g.wx.StaticText(book,label='book tags')
	tags=g.wx.TextCtrl(book,style=g.wx.TE_MULTILINE|g.wx.TE_READONLY)
	tags.SetValue(worktags)
	sizer.Add(tagslabel,0)
	sizer.Add(tags,0)
	book.SetSizerAndFit(sizer)
	