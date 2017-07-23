from django.contrib import admin

from .models import Season, Player, Skaterseasons, Goalieseasons
# Register your models here.
admin.site.register(Season)
admin.site.register(Player)
admin.site.register(Skaterseasons)
admin.site.register(Goalieseasons)