from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=20)
    

    class Meta:
        abstract = True


class Passenger(Person):
    avg_rating = models.FloatField(default=0.0)
    number_of_rides = models.IntegerField(default=0)

    class Meta:
        abstract = False


class Driver(Person):
    avg_rating = models.FloatField(default=0.0)
    vehicle_info = models.CharField(max_length=255)
    number_of_rides = models.IntegerField(default=0)

    class Meta:
        abstract = False


class Admin(Person):
    class Meta:
        abstract = False
