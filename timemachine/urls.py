from django.conf.urls import url
from . import views

app_name = 'timemachine'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^skaterstats/$', views.skaterstats, name='skaterstats'),
	url(r'^goaliestats/$', views.goaliestats, name='goaliestats'),
	url(r'^comparator/$', views.comparator, name='comparator'),
]