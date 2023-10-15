from django.contrib import admin
from .models import Servers

@admin.register(Servers)
class ServersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'config',
        'channel',
        'date',
    ]