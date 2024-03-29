from django.urls import path, include
from .api import RoomReservationViewSet, RoomReservationSuccessViewSet, RoomCheckInViewSet, RoomCheckOutViewSet, AddRoomReviewViewSet
from knox import views as knox_views

urlpatterns = [
    path('api/room_reservations', RoomReservationViewSet.as_view()),
    path('api/room_reservations/payment_success', RoomReservationSuccessViewSet.as_view()),
    path('api/room_reservations/check_in', RoomCheckInViewSet.as_view()),
    path('api/room_reservations/check_out', RoomCheckOutViewSet.as_view()),
    path('api/room_reservations/add_review', AddRoomReviewViewSet.as_view()),
]