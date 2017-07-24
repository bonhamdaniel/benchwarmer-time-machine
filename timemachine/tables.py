import django_tables2 as tables
import itertools
from itertools import chain
from .models import Season, Skaterseasons, Goalieseasons

#class ConvertedPTable(tables.Table):
#	class Meta:
#		model = Convertedsseasons

class CenterColumn(tables.Column):
	def render(self, value):
		return '%d' % value

class ConvertedPTable(tables.Table):
	rank = CenterColumn(attrs = {'td': {'class': 'center'}}, empty_values=(), verbose_name='#')
	player = tables.Column(attrs = {'td': {'class': 'player'}})
	season = tables.Column(attrs = {'td': {'class': 'center'}})
	position = tables.Column(attrs = {'td': {'class': 'center'}}, verbose_name='Pos')
	gp = CenterColumn(attrs = {'td': {'class': 'center'}}, verbose_name='GP')
	g = CenterColumn(attrs = {'td': {'class': 'center'}})
	a = CenterColumn(attrs = {'td': {'class': 'center'}})
	p = CenterColumn(attrs = {'td': {'class': 'center'}})
	pim = CenterColumn(attrs = {'td': {'class': 'center'}}, verbose_name='PIM')
	s = CenterColumn(attrs = {'td': {'class': 'center'}})
	gpg = tables.Column(attrs = {'td': {'class': 'center'}}, verbose_name='G/GP')
	apg = tables.Column(attrs = {'td': {'class': 'center'}}, verbose_name='A/GP')
	pperg = tables.Column(attrs = {'td': {'class': 'center'}}, verbose_name='P/GP')
	evg = CenterColumn(attrs = {'td': {'class': 'center'}}, verbose_name='EVG')
	eva = CenterColumn(attrs = {'td': {'class': 'center'}}, verbose_name='EVA')
	evp = CenterColumn(attrs = {'td': {'class': 'center'}}, verbose_name='EVP')
	ppg = CenterColumn(attrs = {'td': {'class': 'center'}}, verbose_name='PPG')
	ppa = CenterColumn(attrs = {'td': {'class': 'center'}}, verbose_name='PPA')
	ppp = CenterColumn(attrs = {'td': {'class': 'center'}}, verbose_name='PPP')
	shg = CenterColumn(attrs = {'td': {'class': 'center'}}, verbose_name='SHG')
	sha = CenterColumn(attrs = {'td': {'class': 'center'}}, verbose_name='SHA')
	shp = CenterColumn(attrs = {'td': {'class': 'center'}}, verbose_name='SHP')

	def __init__(self, *args, **kwargs):
		super(ConvertedPTable, self).__init__(*args, **kwargs)
		self.counter = itertools.count()
		next(self.counter)

	def render_rank(self):
		return '%d' % next(self.counter)

class ConvertedGTable(tables.Table):
	rank = CenterColumn(attrs = {'td': {'class': 'center'}}, empty_values=(), verbose_name='#')
	player = tables.Column(attrs = {'td': {'class': 'player'}})
	season = tables.Column(attrs = {'td': {'class': 'center'}})
	gp = CenterColumn(attrs = {'td': {'class': 'center'}}, verbose_name='GP')
	toi = tables.Column(attrs = {'td': {'class': 'toi'}}, verbose_name='TOI')
	w = tables.Column(attrs = {'td': {'class': 'center'}}, verbose_name='W')
	l = tables.Column(attrs = {'td': {'class': 'center'}}, verbose_name='L')
	sa = tables.Column(attrs = {'td': {'class': 'center'}}, verbose_name='SA')
	sv = tables.Column(attrs = {'td': {'class': 'center'}}, verbose_name='SV')
	sa_60 = tables.Column(attrs = {'td': {'class': 'center'}}, verbose_name='SA/60')
	gaa = tables.Column(attrs = {'td': {'class': 'center'}}, verbose_name='GAA')
	svpct = tables.Column(attrs = {'td': {'class': 'center'}}, verbose_name='SVPCT')

	def __init__(self, *args, **kwargs):
		super(ConvertedGTable, self).__init__(*args, **kwargs)
		self.counter = itertools.count()
		next(self.counter)

	def render_rank(self):
		return '%d' % next(self.counter)

def convertPData(baseData, base, target):
	data = []
	evAdj = target.evg_gp / base.evg_gp
	ppAdj = target.ppg_gp / base.ppg_gp
	shAdj = target.shg_gp / base.shg_gp
	sAdj = target.s_gp / base.s_gp
	pimAdj = target.pim_gp / base.pim_gp
	aAdj = target.a_gp / base.a_gp
	for p in baseData:
		evg = int((p.goals - p.ppg - p.shg) * evAdj)
		eva = int((p.assists - p.ppa - p.sha) * evAdj)
		ppg = int(p.ppg * ppAdj)
		ppa = int(p.ppa * ppAdj)
		shg = int(p.shg * shAdj)
		sha = int(p.sha * shAdj)
		pim = int(p.pim * pimAdj)
		s = int(p.shots * sAdj)
		g=evg+ppg+shg
		a=eva+ppa+sha
		pts=evg+ppg+shg+eva+ppa+sha
		evp=evg+eva
		ppp=ppg+ppa
		shp=shg+sha
		gpg = g / p.gp
		apg = a / p.gp
		pperg = pts / p.gp
		data.append({"player": p.playerid.playername, "season": base.seasonid, "position": p.playerid.position, "gp": p.gp, "g": g, "a": a, "p": pts, "pim": pim, "s": s, "gpg": '{0:.2f}'.format(gpg), "apg": '{0:.2f}'.format(apg), "pperg": '{0:.2f}'.format(pperg), "evg": evg, "eva": eva, "evp": evp, "ppg": ppg, "ppa": ppa, "ppp": ppp, "shg": shg, "sha": sha, "shp": shp})
	return data

def convertGData(baseData, base, target):
	data = []
	gAdj = target.g_gp / base.g_gp
	sAdj = target.s_gp / base.s_gp
	svAdj = ((target.s - target.g) / target.s) / ((base.s - base.g) / base.s)
	for p in baseData:
		if p.sa > 0 and p.sv > 0:
			w = int(p.w - p.sow)
			l = int(p.l - p.sol)
			sa = int(p.sa * sAdj)
			svpct = p.sv/p.sa
			sv = int(sa * svpct)
			sv = int(sv * svAdj)
			gaa = (sa-sv) / p.toi * 60
			svpct = sv / sa
			sa_60 = sa / p.toi * 60
			data.append({'player': p.playerid.playername, "season": base.seasonid, 'gp': p.gp, 'toi': '{0:.2f}'.format(p.toi), 'w': w, 'l': l, 'sa': sa, 'sv': int(sv), 'sa_60': '{0:.2f}'.format(sa_60), 'gaa': '{0:.2f}'.format(gaa), 'svpct': '{0:.3f}'.format(svpct)})
	return data

def convertCData(target, player1Data, player2Data):
	data = []
	playerSeasons = list(chain(player1Data, player2Data))
	for p in playerSeasons:
		base = Season.objects.get(pk=str(p.seasonid)[:8])
		evAdj = target.evg_gp / base.evg_gp
		ppAdj = target.ppg_gp / base.ppg_gp
		shAdj = target.shg_gp / base.shg_gp
		sAdj = target.s_gp / base.s_gp
		pimAdj = target.pim_gp / base.pim_gp
		aAdj = target.a_gp / base.a_gp
		evg = int((p.goals - p.ppg - p.shg) * evAdj)
		eva = int((p.assists - p.ppa - p.sha) * evAdj)
		ppg = int(p.ppg * ppAdj)
		ppa = int(p.ppa * ppAdj)
		shg = int(p.shg * shAdj)
		sha = int(p.sha * shAdj)
		pim = int(p.pim * pimAdj)
		s = int(p.shots * sAdj)
		g=evg+ppg+shg
		a=eva+ppa+sha
		pts=evg+ppg+shg+eva+ppa+sha
		evp=evg+eva
		ppp=ppg+ppa
		shp=shg+sha
		gpg = g / p.gp
		apg = a / p.gp
		pperg = pts / p.gp
		data.append({"player": p.playerid.playername, "season": base.seasonid, "position": p.playerid.position, "gp": p.gp, "g": g, "a": a, "p": pts, "pim": pim, "s": s, "gpg": '{0:.2f}'.format(gpg), "apg": '{0:.2f}'.format(apg), "pperg": '{0:.2f}'.format(pperg), "evg": evg, "eva": eva, "evp": evp, "ppg": ppg, "ppa": ppa, "ppp": ppp, "shg": shg, "sha": sha, "shp": shp})
	return data

def convertCarData(target, player1Data, player2Data):
	data = []
	evg = 0
	eva = 0
	evp = 0
	ppg = 0
	ppa = 0
	ppp = 0
	shg = 0
	sha = 0
	shp = 0
	pim = 0
	s = 0
	g = 0
	a = 0
	pts = 0
	gp = 0
	minY = int(player1Data[0].seasonid)
	maxY = int(player1Data[0].seasonid)
	for p in player1Data:
		if int(p.seasonid) < minY:
			miny = int(p.seasonid) 
		if int(p.seasonid) > maxY:
			maxy = int(p.seasonid) 
		base = Season.objects.get(pk=str(p.seasonid)[:8])
		evAdj = target.evg_gp / base.evg_gp
		ppAdj = target.ppg_gp / base.ppg_gp
		shAdj = target.shg_gp / base.shg_gp
		sAdj = target.s_gp / base.s_gp
		pimAdj = target.pim_gp / base.pim_gp
		aAdj = target.a_gp / base.a_gp
		evg += int((p.goals - p.ppg - p.shg) * evAdj)
		eva += int((p.assists - p.ppa - p.sha) * evAdj)
		ppg += int(p.ppg * ppAdj)
		ppa += int(p.ppa * ppAdj)
		shg += int(p.shg * shAdj)
		sha += int(p.sha * shAdj)
		pim += int(p.pim * pimAdj)
		s += int(p.shots * sAdj)
		gp += p.gp
	g+=evg+ppg+shg
	a+=eva+ppa+sha
	pts+=evg+ppg+shg+eva+ppa+sha
	evp+=evg+eva
	ppp+=ppg+ppa
	shp+=shg+sha
	gpg = g / gp
	apg = a / gp
	pperg = pts / gp
	season = str(miny)[:4] + str(maxY)[4:8]
	data.append({"player": p.playerid.playername, "season": season, "position": p.playerid.position, "gp": gp, "g": g, "a": a, "p": pts, "pim": pim, "s": s, "gpg": '{0:.2f}'.format(gpg), "apg": '{0:.2f}'.format(apg), "pperg": '{0:.2f}'.format(pperg), "evg": evg, "eva": eva, "evp": evp, "ppg": ppg, "ppa": ppa, "ppp": ppp, "shg": shg, "sha": sha, "shp": shp})
	evg = 0
	eva = 0
	evp = 0
	ppg = 0
	ppa = 0
	ppp = 0
	shg = 0
	sha = 0
	shp = 0
	pim = 0
	s = 0
	g = 0
	a = 0
	pts = 0
	gp = 0
	minY = int(player2Data[0].seasonid)
	maxY = int(player2Data[0].seasonid)
	for p in player2Data:
		if int(p.seasonid) < minY:
			miny = int(p.seasonid) 
		if int(p.seasonid) > maxY:
			maxy = int(p.seasonid) 
		base = Season.objects.get(pk=p.seasonid)
		evAdj = target.evg_gp / base.evg_gp
		ppAdj = target.ppg_gp / base.ppg_gp
		shAdj = target.shg_gp / base.shg_gp
		sAdj = target.s_gp / base.s_gp
		pimAdj = target.pim_gp / base.pim_gp
		aAdj = target.a_gp / base.a_gp
		evg += int((p.goals - p.ppg - p.shg) * evAdj)
		eva += int((p.assists - p.ppa - p.sha) * evAdj)
		ppg += int(p.ppg * ppAdj)
		ppa += int(p.ppa * ppAdj)
		shg += int(p.shg * shAdj)
		sha += int(p.sha * shAdj)
		pim += int(p.pim * pimAdj)
		s += int(p.shots * sAdj)
		gp += p.gp
	g+=evg+ppg+shg
	a+=eva+ppa+sha
	pts+=evg+ppg+shg+eva+ppa+sha
	evp+=evg+eva
	ppp+=ppg+ppa
	shp+=shg+sha
	gpg = g / gp
	apg = a / gp
	pperg = pts / gp
	season = str(miny)[:4] + str(maxY)[4:8]
	data.append({"player": p.playerid.playername, "season": season, "position": p.playerid.position, "gp": gp, "g": g, "a": a, "p": pts, "pim": pim, "s": s, "gpg": '{0:.2f}'.format(gpg), "apg": '{0:.2f}'.format(apg), "pperg": '{0:.2f}'.format(pperg),  "evg": evg, "eva": eva, "evp": evp, "ppg": ppg, "ppa": ppa, "ppp": ppp, "shg": shg, "sha": sha, "shp": shp})
	return data
