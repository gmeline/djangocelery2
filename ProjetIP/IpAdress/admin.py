from django.contrib import admin
from .models import Server,Command, IP

admin.site.register(Server)
admin.site.register(Command)
admin.site.register(IP)
