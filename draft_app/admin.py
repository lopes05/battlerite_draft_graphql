from django.contrib import admin

# Register your models here.
from .models import *

class ChampionAdmin(admin.ModelAdmin):
    pass


class MapAdmin(admin.ModelAdmin):
    pass


admin.site.register(Champion, ChampionAdmin)
admin.site.register(Map, MapAdmin)