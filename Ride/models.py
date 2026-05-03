from django.db import models

# Create your models here.
class Ride(models.Model):
    id = models.AutoField(primary_key=True)
    driver_id = models.ForeignKey('Authentication.Driver', on_delete=models.CASCADE)
    departure_location = models.CharField(max_length=255)
    arrival_location = models.CharField(max_length=255)
    departure_date_time = models.DateTimeField()
    available_seats = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
 
    

   