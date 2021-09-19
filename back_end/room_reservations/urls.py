from django.urls import path, include
from .api import RoomReservationViewSet
from knox import views as knox_views

urlpatterns = [
    path('api/room_reservations', RoomReservationViewSet.as_view()),
]