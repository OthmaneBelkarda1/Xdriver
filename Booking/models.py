from django.db import models
import datetime
from Authentication.models import Driver, Passenger
from Ride.models import Ride

# Create your models here.class
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    ride = models.ForeignKey('Ride.Ride', on_delete=models.CASCADE)
    passenger = models.ForeignKey('Authentication.Passenger', on_delete=models.CASCADE)
    booking_date_time = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=20.0)
    
