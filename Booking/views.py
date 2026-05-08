from datetime import datetime
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from Authentication.models import Driver,Passenger
from Ride.models import Ride
from django.utils.dateparse import parse_datetime
from Booking.models import Booking
from django.shortcuts import render

# Create your views here.
@csrf_exempt
@require_http_methods(["POST"])
def Book_Ride(request):
    try:
     data=json.loads(request.body)
     Passenger_id=data.get('passenger_id')
     Ride_id=data.get('ride_id')
     if not Passenger_id or not Ride_id:
        return JsonResponse({"error": "passenger_id and ride_id are required"}, status=400)
     if not Passenger.objects.filter(id=Passenger_id).exists():
        return JsonResponse({"error": "Passenger not found"}, status=404)
     if not Ride.objects.filter(id=Ride_id).exists():
        return JsonResponse({"error": "Ride not found"}, status=404)
     ride = Ride.objects.get(id=Ride_id)
     passenger = Passenger.objects.get(id=Passenger_id)
     booking = Booking.objects.create(
        ride_id=ride.id,
        passenger_id=passenger.id
    )
     Ride.objects.filter(id=Ride_id).update(available_seats=ride.available_seats - 1)
    except Exception as e:
        return JsonResponse({"invalid Json": str(e)}, status=500) 
    return JsonResponse({"message": "Ride booked successfully"}, status=201)

@csrf_exempt
@require_http_methods(["GET"])
def viewRideHistoryByID(request, id):
    try:
        bookings = Booking.objects.filter(passenger_id=id)
        if not bookings.exists():
            return JsonResponse({"error": "No booking history found for this passenger"}, status=404)
        history = []
        for booking in bookings:
            ride = Ride.objects.get(id=booking.ride_id)
            driver=Driver.objects.get(id=ride.driver_id)
            history.append({
                "ride_id": ride.id,
                "departure":ride.departure_location,
                "arrival": ride.arrival_location,
                "driver_First_Name": driver.first_name,
                "driver_Last_Name": driver.last_name
            })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"history": history}, status=200)

