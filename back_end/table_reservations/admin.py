from django.contrib import admin
from .models import TableReservation

class TableReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'customer', 'meal_time', 'customer_arrival', 'reserved_date', 'num_of_people', 'date_added')
    list_display_links = ('id', 'restaurant')
    list_filter = ('restaurant', 'customer', 'customer_arrival', 'meal_time')
    search_fields = ('meal_time',)
    list_per_page = 25

admin.site.register(TableReservation, TableReservationAdmin)
