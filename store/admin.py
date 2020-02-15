from django.contrib import admin

from .models import Products
from .models import BusinesZone 
from .models import GigZone
from .models import GameZone


admin.site.register(Products)
admin.site.register(BusinesZone)
admin.site.register(GigZone)
admin.site.register(GameZone)
