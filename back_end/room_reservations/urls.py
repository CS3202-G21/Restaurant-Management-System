from rest_framework import routers
from .api import RoomViewSet

router = routers.DefaultRouter()
router.register('api/room_reservations', RoomViewSet, 'room_reservations')

urlpatterns = router.urls
