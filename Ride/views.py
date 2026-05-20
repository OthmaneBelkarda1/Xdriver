from datetime import datetime

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from Authentication.models import Driver
from django.utils.dateparse import parse_datetime

from .models import Ride


@csrf_exempt
@require_http_methods(["POST"])
def publish_Ride(request):
    try:
        data = json.loads(request.body)

        driver_id = data.get('driver_id')

        if not driver_id:
            return JsonResponse({"error": "driver_id is required"}, status=400)

        try:
            driver = Driver.objects.get(id=driver_id)
        except Driver.DoesNotExist:
            return JsonResponse({"error": "Driver not found"}, status=404)

        ride = Ride.objects.create(
            driver=driver,
            departure_location=data.get('departure_location'),
            arrival_location=data.get('arrival_location'),
            departure_date_time=parse_datetime(data.get('departure_date_time')),
            available_seats=data.get('available_seats'),
            distance=data.get('distance')
        )

        return JsonResponse({
            "status": "success",
            "ride_id": ride.id
        })

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
   
@require_http_methods(["GET"])
def viewRideHistory(request, id):
    try:
        # Filter rides by driver_id
        rides = Ride.objects.filter(driver_id=id)

        # Convert queryset to list of dictionaries
        rides_data = []
        for ride in rides:
            rides_data.append({
                "id": ride.id,
                "departure_location": ride.departure_location,
                "arrival_location": ride.arrival_location,
                "departure_date_time": ride.departure_date_time,
                "available_seats": ride.available_seats,
                "distance": str(ride.distance)  # Decimal → string for JSON
            })

        return JsonResponse({
            "status": "success",
            "data": rides_data
        })

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)
    
@require_http_methods(["GET"])
def SearchForRide(request, departure, arrival, date):
    try:
        # Parse date (DD-MM-YYYY)
        parsed_date = datetime.strptime(date, "%d-%m-%Y").date()

        rides = Ride.objects.filter(
            departure_location__iexact=departure,
            arrival_location__iexact=arrival,
            departure_date_time__date=parsed_date
        )

        rides_data = list(rides.values(
            "id",
            "departure_location",
            "arrival_location",
            "departure_date_time",
            "available_seats",
            "distance"
        ))

        return JsonResponse({
            "status": "success",
            "count": len(rides_data),
            "data": rides_data
        })

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)  
    
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_ride(request):
    try:
        if request.method != "DELETE":
            return JsonResponse({
                "status": "error",
                "message": "Only DELETE method allowed"
            }, status=405)

        data = json.loads(request.body)
        ride_id = data.get("ride_id")
        driver_id = data.get("driver_id")

        ride = Ride.objects.get(id=ride_id)

       
        if ride.driver_id.id != driver_id:
            return JsonResponse({
                "status": "error",
                "message": "You are not allowed to delete this ride"
            }, status=403)

        ride.delete()

        return JsonResponse({
            "status": "success",
            "message": "Ride deleted successfully"
        })

    except Ride.DoesNotExist:
        return JsonResponse({
            "status": "error",
            "message": "Ride not found"
        }, status=404)

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)
    
@csrf_exempt
def edit_ride(request):
    try:
        if request.method != "PUT":
            return JsonResponse({
                "status": "error",
                "message": "Only PUT method allowed"
            }, status=405)

        data = json.loads(request.body)

        ride_id = data.get("ride_id")
        driver_id = data.get("driver_id")

        ride = Ride.objects.get(id=ride_id)

        #  security check
        if ride.driver_id != driver_id:
            return JsonResponse({
                "status": "error",
                "message": "You are not allowed to edit this ride"
            }, status=403)

        #  update fields if provided
        if "departure_location" in data:
            ride.departure_location = data["departure_location"]

        if "arrival_location" in data:
            ride.arrival_location = data["arrival_location"]

        if "departure_date_time" in data:
            ride.departure_date_time = datetime.strptime(
                data["departure_date_time"],
                "%Y-%m-%d %H:%M:%S"
            )

        if "available_seats" in data:
            ride.available_seats = data["available_seats"]

        if "distance" in data:
            ride.distance = data["distance"]

        ride.save()

        return JsonResponse({
            "status": "success",
            "message": "Ride updated successfully"
        })

    except Ride.DoesNotExist:
        return JsonResponse({
            "status": "error",
            "message": "Ride not found"
        }, status=404)

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)    
    
