from libs import globals as g

def load(url):
	work = g.AO3.Work(g.AO3.utils.workid_from_url(url))
	worktext=''
	workstats=f'Authors: {work.authors}\nChapters: {work.nchapters}\nWords: {work.words}\nHits: {work.hits}\nKudos: {work.kudos}\nBookmarks: {work.bookmarks}'
	worktags=''
	for i in work.tags:
		worktags=worktags+i+'\n'
	if worktags=='':
		worktags='no tags available'
	workfandoms=''
	for i in work.fandoms:
		workfandoms=workfandoms+i+'\n'
	if workfandoms=='':
		workfandoms='no fandoms available for this work'
	worksummery=work.summary
	book=g.wx.Panel(g.notebook)
	g.notebook.AddPage(book, work.title)
	sizer=g.wx.BoxSizer()
	titlelabel=g.wx.StaticText(book,label='title')
	title=g.wx.TextCtrl(book,style=g.wx.TE_MULTILINE|g.wx.TE_DONTWRAP|g.wx.TE_READONLY)
	title.SetValue(work.title)
	sizer.Add(titlelabel,0)
	sizer.Add(title)
	summerylabel=g.wx.StaticText(book,label='summery')
	summery=g.wx.TextCtrl(book,style=g.wx.TE_MULTILINE|g.wx.TE_READONLY|g.wx.TE_DONTWRAP)
	summery.SetValue(worksummery)
	sizer.Add(summerylabel,0)
	sizer.Add(summery)
	statslabel=g.wx.StaticText(book,label='book stats')
	stats=g.wx.TextCtrl(book,style=g.wx.TE_MULTILINE|g.wx.TE_READONLY|g.wx.TE_DONTWRAP)
	stats.SetValue(workstats)
	sizer.Add(statslabel,0)
	sizer.Add(stats,0)
	tagslabel=g.wx.StaticText(book,label='book tags')
	tags=g.wx.TextCtrl(book,style=g.wx.TE_MULTILINE|g.wx.TE_READONLY|g.wx.TE_DONTWRAP)
	tags.SetValue(worktags)
	sizer.Add(tagslabel,0)
	sizer.Add(tags,0)
	fandomslabel=g.wx.StaticText(book,label='book fandoms')
	fandoms=g.wx.TextCtrl(book,style=g.wx.TE_MULTILINE|g.wx.TE_READONLY|g.wx.TE_DONTWRAP)
	fandoms.SetValue(workfandoms)
	sizer.Add(fandomslabel,0)
	sizer.Add(fandoms,0)
	book.SetSizerAndFit(sizer)

	