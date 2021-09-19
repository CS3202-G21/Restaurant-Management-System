from .models import RoomReservation
from rooms.models import Room
from room_types.models import RoomType
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import RoomReservationSerializer
from datetime import datetime, date
from rest_framework import serializers


# Room Reservation ViewSet
class RoomReservationViewSet(generics.GenericAPIView):
    queryset = RoomReservation.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoomReservationSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        data['total_price'], start_date, end_date = get_total_price(data)

        if are_dates_booked(start_date, end_date, data['room']):
            raise serializers.ValidationError("Given Dates are Booked")

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        room_reservation = serializer.save()

        return Response({
            "room_reservation": RoomReservationSerializer(room_reservation, context=self.get_serializer_context()).data
        })


def get_total_price(data):
    room_type = Room.objects.filter(id=data['room'])[0].type_id
    room_price = RoomType.objects.filter(id=room_type)[0].price

    s_y, s_m, s_d = list(map(int, data['start_date'][:10].strip().split('-')))
    s_h, s_mi, s_s = list(map(int, data['start_date'][11:].strip().split(':')))
    e_y, e_m, e_d = list(map(int, data['end_date'][:10].strip().split('-')))
    e_h, e_mi, e_s = list(map(int, data['end_date'][11:].strip().split(':')))

    num_of_days = date(e_y, e_m, e_d) - date(s_y, s_m, s_d)

    return num_of_days.days * float(str(room_price)), datetime(s_y, s_m, s_d, s_h, s_mi, s_s), datetime(e_y, e_m, e_d, e_h, e_mi, e_s)


def are_dates_booked(start_date, end_date, room_id):
    prev_reservations_from_start = RoomReservation.objects.filter(room=room_id, start_date__lte=start_date, end_date__gt=start_date)
    if len(prev_reservations_from_start) == 0:
        prev_reservations_from_end = RoomReservation.objects.filter(room=room_id, start_date__lt=end_date, end_date__gte=end_date)
        if len(prev_reservations_from_end) == 0:
            return False
    return True
