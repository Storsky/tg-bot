from django.contrib import admin
from .models import *

class DepartureAdmin(admin.TabularInline):
    fk_name = 'from_thread'
    model = Thread_Trigger

class DestinationAdmin(admin.TabularInline):
    fk_name = 'to_thread'
    model = Thread_Trigger

class ThreadAdmin(admin.ModelAdmin):
    model = Thread
    fields = ['name', 'text']
    inlines = [DepartureAdmin, DestinationAdmin,]


class PlayerAdmin(admin.ModelAdmin):
    model = Player



admin.site.register(Thread, ThreadAdmin)
admin.site.register(Player, PlayerAdmin)


