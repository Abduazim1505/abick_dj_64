from django.contrib import admin

from .models import *

class AutoSalonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'context', 'created_at', 'updated_at')
    list_display_links = ['title']
    search_fields = ['title']

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'price', 'year')
    list_display_links = ['model']
    search_fields = ['model']

admin.site.register(AutoSalon, AutoSalonAdmin)
admin.site.register(Car, CarAdmin)