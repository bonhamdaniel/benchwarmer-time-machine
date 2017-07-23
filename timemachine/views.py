from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django_tables2 import RequestConfig
from django.apps import apps
from .tables import ConvertedPTable, convertPData, ConvertedGTable, convertGData, convertCData, convertCarData

from .models import Skaterseasons, Goalieseasons, Season, Player

# Create your views here.
class IndexView(generic.ListView):
	model = Player
	template_name = 'timemachine/index.html'

def  goaliestats(request):
	# set menus
	base = Season.objects.get(pk=request.GET['baseSeason'])
	target = Season.objects.get(pk=request.GET['targetSeason'])
	season1 = Season.objects.order_by('seasonid')
	season2 = Season.objects.order_by('seasonid')
	# prepare data
	baseData = Goalieseasons.objects.filter(seasonid=str(request.GET['baseSeason']))
	data = convertGData(baseData, base, target)
	if 'include' in request.GET:
		baseData = Goalieseasons.objects.filter(seasonid=str(request.GET['targetSeason']))
		data += (convertGData(baseData, target, target))
	table = ConvertedGTable(data, order_by='-w')
	table.paginate(page=request.GET.get('page', 1), per_page=30)
	RequestConfig(request, paginate={'per_page': 30}).configure(table)
	return render(request, 'timemachine/goaliestats.html', {'base': base, 'target': target, 'season1': season1, 'season2': season2, 'table': table})

def  skaterstats(request):
	# set menus
	base = Season.objects.get(pk=request.GET['baseSeason'])
	target = Season.objects.get(pk=request.GET['targetSeason'])
	season1 = Season.objects.order_by('seasonid')
	season2 = Season.objects.order_by('seasonid')
	# prepare data
	baseData = Skaterseasons.objects.filter(seasonid=str(request.GET['baseSeason']))
	data = convertPData(baseData, base, target)
	if 'include' in request.GET:
		baseData = Skaterseasons.objects.filter(seasonid=str(request.GET['targetSeason']))
		data += (convertPData(baseData, target, target))
	table = ConvertedPTable(data, order_by='-p')
	RequestConfig(request, paginate={'per_page': 35}).configure(table)
	return render(request, 'timemachine/skaterstats.html', {'base': base, 'target': target, 'season1': season1, 'season2': season2, 'table': table})

def  comparator(request):
	# set menus
	base = Season.objects.get(pk=request.GET['baseSeason'])
	season1 = Season.objects.order_by('seasonid')
	players1 = Player.objects.order_by('playername')
	players2 = Player.objects.order_by('playername')
	# prepare data
	player1Data = Skaterseasons.objects.filter(playerid=str(request.GET['player1']))
	player2Data = Skaterseasons.objects.filter(playerid=str(request.GET['player2']))
	player1 = Player.objects.get(pk=(request.GET['player1']))
	player2 = Player.objects.get(pk=(request.GET['player2']))
	if 'seasons' in request.GET:
		data = convertCData(base, player1Data, player2Data)
	else:		
		data = convertCarData(base, player1Data, player2Data)
	table = ConvertedPTable(data, order_by='-p')
	RequestConfig(request, paginate={'per_page': 35}).configure(table)
	return render(request, 'timemachine/comparator.html', {'base': base, 'season1': season1, 'players1': players1, 'players2': players2, 'player1': player1, 'player2': player2, 'table': table})