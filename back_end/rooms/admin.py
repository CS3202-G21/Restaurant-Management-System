from django.contrib import admin

from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_no', 'type', 'status', 'price')
    list_display_links = ('id', 'room_no')
    list_filter = ('floor_no',)
    search_fields = ('room_no', 'floor_no', 'description', 'type', 'status', 'price', 'price')
    list_per_page = 25

admin.site.register(Room, RoomAdmin)
