from django.contrib import admin

from .models import Season, Game, Player, Team, Skaterseasons, Goalieseasons, Convertedsseasons
# Register your models here.
admin.site.register(Season)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Skaterseasons)
admin.site.register(Goalieseasons)
admin.site.register(Convertedsseasons)