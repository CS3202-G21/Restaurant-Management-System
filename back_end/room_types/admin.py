from django.contrib import admin

from .models import RoomType

class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', 'title')
    list_filter = ('title', 'price')
    search_fields = ('title', 'price', 'description', 'number_of_adults', 'number_of_beds')
    list_per_page = 25

admin.site.register(RoomType, RoomTypeAdmin)
