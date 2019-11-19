from django.contrib import admin
from .models import Player
from .models import Room


# Register your models here.
admin.site.register(Player)
admin.site.register(Room)