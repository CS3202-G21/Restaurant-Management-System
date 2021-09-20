from .models import TableReservation
from restaurants.models import Restaurant
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import TableReservationSerializer
from datetime import datetime, date
from rest_framework import serializers
from django.db.models import Sum


# Table Reservation ViewSet
class TableReservationViewSet(generics.GenericAPIView):
    # TODO check if customer

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TableReservationSerializer

    def get(self, request):
        table_reservations_objs = TableReservation.objects.filter(customer=request.user.id)
        table_reservations = []

        for obj in table_reservations_objs:
            reservation = obj.__dict__
            reservation.pop('_state')
            table_reservations.append(reservation)

        return Response({"table_reservations": table_reservations})

    def post(self, request, *args, **kwargs):
        BREAKFAST = 'breakfast'
        LUNCH = 'lunch'
        DINNER = 'dinner'
        meal_times = (
            (BREAKFAST, 'Breakfast'),
            (LUNCH, 'Lunch'),
            (DINNER, 'Dinner')
        )

        data = request.data
        data['customer'] = request.user.id
        data['meal_time'] = meal_times[data['meal_time']][0]

        if is_fully_booked(data['restaurant'], data['reserved_date'], data['meal_time'], data['num_of_people']):
            raise serializers.ValidationError("Restaurant is Out of Capacity")

        if not is_meal_time_served_by_restaurant(data['restaurant'], data['meal_time']):
            raise serializers.ValidationError("Restaurant does not supply "+data['meal_time'])

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        table_reservation = serializer.save()

        return Response({
            "room_reservation": TableReservationSerializer(table_reservation, context=self.get_serializer_context()).data
        })


# View Set to get the available reservations for today
class GetTodayTableReservationsViewSet(generics.GenericAPIView):
    # TODO check if waiter
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TableReservationSerializer

    def get(self, request):
        BREAKFAST = 'breakfast'
        LUNCH = 'lunch'
        DINNER = 'dinner'
        meal_times = (
            (BREAKFAST, 'Breakfast'),
            (LUNCH, 'Lunch'),
            (DINNER, 'Dinner')
        )

        today = datetime.now().date()
        time_now = datetime.now().time()

        breakfast_begin = time_now.replace(hour=6, minute=0, second=0, microsecond=0)
        breakfast_end = time_now.replace(hour=10, minute=30, second=0, microsecond=0)
        lunch_begin = time_now.replace(hour=12, minute=0, second=0, microsecond=0)
        lunch_end = time_now.replace(hour=15, minute=30, second=0, microsecond=0)
        dinner_begin = time_now.replace(hour=19, minute=30, second=0, microsecond=0)
        dinner_end = time_now.replace(hour=22, minute=30, second=0, microsecond=0)

        if breakfast_begin <= time_now <= breakfast_end:
            table_reservations_objs = TableReservation.objects.filter(reserved_date=today, meal_time=BREAKFAST)
        elif lunch_begin <= time_now <= lunch_end:
            table_reservations_objs = TableReservation.objects.filter(reserved_date=today, meal_time=LUNCH)
        elif dinner_begin <= time_now <= dinner_end:
            table_reservations_objs = TableReservation.objects.filter(reserved_date=today, meal_time=DINNER)
        else:
            raise serializers.ValidationError("No Meal Provided at this Time.")
        table_reservations = []

        for obj in table_reservations_objs:
            reservation = obj.__dict__
            reservation.pop('_state')
            table_reservations.append(reservation)

        return Response({"table_reservations": table_reservations})


# View Set to get update customer arrival
class TableReservationArrivalViewSet(generics.GenericAPIView):
    # TODO check if waiter
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TableReservationSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        reservation_id = data['reservation_id']

        try:
            reservation = TableReservation.objects.get(id=reservation_id, customer=request.user.id)
        except TableReservation.DoesNotExist:
            raise serializers.ValidationError("Invalid Access")

        if datetime.now().date() == reservation.reserved_date:
            reservation.customer_arrival = True
            reservation.save()
        else:
            raise serializers.ValidationError("Today is not the Reserved Date.")

        return Response({
            "room_reservation": TableReservationSerializer(reservation, context=self.get_serializer_context()).data
        })


def is_fully_booked(restaurant, reserved_date, meal_time, num_of_people):
    try:
        restaurant_max_people = Restaurant.objects.filter(id=restaurant)[0].max_number_of_people_for_reservation
    except IndexError:
        raise serializers.ValidationError('Invalid Restaurant')

    prev_reservations = TableReservation.objects.filter(restaurant=restaurant, reserved_date=reserved_date, meal_time=meal_time).aggregate(Sum('num_of_people'))['num_of_people__sum']

    if prev_reservations and restaurant_max_people >= prev_reservations + num_of_people:
        return False
    elif restaurant_max_people >= num_of_people:
        return False
    return True


def is_meal_time_served_by_restaurant(restaurant, meal_time):
    if meal_time == 'breakfast':
        return Restaurant.objects.filter(id=restaurant)[0].breakfast
    elif meal_time == 'lunch':
        return Restaurant.objects.filter(id=restaurant)[0].lunch
    elif meal_time == 'dinner':
        return Restaurant.objects.filter(id=restaurant)[0].breakfast
    else:
        raise serializers.ValidationError("Invalid Meal Time")