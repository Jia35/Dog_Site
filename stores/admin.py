from django.contrib import admin
from .models import Alluser, Dogs, GPSs, Message


@admin.register(Alluser)
class AlluserAdmin(admin.ModelAdmin):
    list_display = ('account', 'name', 'picture', 'gender', 'phone_number',
                    'residential_location', 'score')
    list_filter = ('gender','residential_location')
    ordering = ('account','score')

@admin.register(Dogs)
class DogsAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'age', 'breed', 'favorite_food', 'is_foster', 'master')
    list_filter = ('master', 'gender', 'breed', 'is_foster')
    #ordering = ('name')

@admin.register(GPSs)
class GPSsAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'latitude', 'longitude', 'dog')
    #list_filter = ('dog')
    #ordering = ('date', 'time')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('account', 'text', 'timestamp')
    #ordering = ('date', 'time')

#admin.site.register(Comment)
