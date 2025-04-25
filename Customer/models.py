from django.db import models


class Passenger(models.Model):
    CITY_CHOICES = [
        ('Akola', 'Akola'),
        ('Amravati', 'Amravati'),
        ('Washim', 'Washim'),
        ('Chennai', 'Chennai'),
        ('Bangalore', 'Bangalore'),
    ]

    full_name = models.CharField(max_length=70)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact_number = models.CharField(max_length=15)
    source_station = models.CharField(max_length=100, choices=CITY_CHOICES)
    destination_station = models.CharField(max_length=100, choices=CITY_CHOICES)
    date_of_journey = models.DateField()

    def __str__(self):
        return self.full_name
