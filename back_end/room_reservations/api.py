from .models import RoomReservation
from rest_framework import viewsets, permissions
from .serializers import RoomReservationSerializer


# Room ViewSet
class RoomViewSet(viewsets.ModelViewSet):
    queryset = RoomReservation.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoomReservationSerializer
