from datetime import datetime
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from Authentication.models import Driver,Passenger
from Ride.models import Ride
from django.utils.dateparse import parse_datetime
from Booking.models import Booking
from .models import Ride
from django.shortcuts import render

# Create your views here.
@csrf_exempt
@require_http_methods(["POST"])
def Book_Ride(request):
    try:
     data=json.loads(request.body)
     Passenger_id=data.get('passenger_id')
     Ride_id=data.get('ride_id')
     if not Passenger or not Ride:
        return JsonResponse({"error": "passenger_id and ride_id are required"}, status=400)
     if not Passenger.objects.filter(id=Passenger_id).exists():
        return JsonResponse({"error": "Passenger not found"}, status=404)
     if not Ride.objects.filter(id=Ride_id).exists():
        return JsonResponse({"error": "Ride not found"}, status=404)
    
     booking = Booking.objects.create(
        ride_id=Ride_id,
        passenger_id=Passenger_id
    )
    except Exception as e:
        return JsonResponse({"invalid Json": str(e)}, status=500) 
    return JsonResponse({"message": "Ride booked successfully"}, status=201)

@csrf_exempt
@require_http_methods(["GET"])
def viewRideHistoryByID(request, id):
    try:
        bookings = Booking.objects.filter(passenger_id=id)
        history = []
        for booking in bookings:
            ride = Ride.objects.get(id=booking.ride_id)
            driver=Driver.objects.get(id=ride.driver_id)
            history.append({
                "ride_id": ride.id,
                "departure": ride.departure,
                "arrival": ride.arrival,
                "date_time": ride.date_time,
                "driver_First_Name": driver.first_name,
                "driver_Last_Name": driver.last_name
            })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"history": history}, status=200)

