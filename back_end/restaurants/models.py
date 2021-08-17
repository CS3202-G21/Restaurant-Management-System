from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Restaurant(models.Model):
    # restaurant status enum
    AVAILABLE = 'available'
    UNAVAILABLE = 'unavailable'
    MAINTENANCE = 'maintenance'
    room_statuses = (
        (AVAILABLE, 'Available'),
        (UNAVAILABLE, 'Unavailable'),
        (MAINTENANCE, 'Maintenance')
    )

    title = models.CharField(max_length=255)
    floor_number = models.IntegerField()
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=room_statuses, default=AVAILABLE)
    number_of_tables = models.IntegerField()
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/restaurants/main')
    photo_1 = models.ImageField(upload_to='photos/restaurants/other', blank=True)
    photo_2 = models.ImageField(upload_to='photos/restaurants/other', blank=True)
    photo_3 = models.ImageField(upload_to='photos/restaurants/other', blank=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    manager_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return str(self.title)
