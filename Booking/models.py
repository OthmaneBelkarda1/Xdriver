from django.db import models
import datetime
from Authentication.models import Driver, Passenger

# Create your models here.class
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    ride_id = models.ForeignKey('Ride.Ride', on_delete=models.CASCADE)
    passenger_id = models.ForeignKey('Authentication.Passenger', on_delete=models.CASCADE)
    booking_date_time = models.DateTimeField(auto_now_add=True)
    