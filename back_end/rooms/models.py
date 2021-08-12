from django.db import models
from datetime import datetime


class Room(models.Model):
    # room types enum
    COMMON = 'common'
    LUXURY = 'luxury'
    room_types = (
        (COMMON, 'Common'),
        (LUXURY, 'Luxury')
    )

    # room status enum
    OCCUPIED = 'occupied'
    VACANT = 'vacant'
    room_statuses = (
        (OCCUPIED, 'Occupied'),
        (VACANT, 'Vacant')
    )

    room_no = models.IntegerField()
    floor_no = models.IntegerField()
    type = models.CharField(max_length=10, choices=room_types, default=COMMON)
    status = models.CharField(max_length=10, choices=room_statuses, default=VACANT)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    num_of_adults = models.IntegerField()
    num_of_beds = models.IntegerField()
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/rooms/')
    photo_1 = models.ImageField(upload_to='photos/rooms/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/rooms/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/rooms/', blank=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    # customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self):
        return str(self.room_no)
