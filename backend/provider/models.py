from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

class IncidentType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return self.name

class Incident(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(IncidentType, on_delete=models.CASCADE)
    month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    location = models.PointField(null=False, blank=False)

    def __str__(self):
        return str(self.id)

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False, blank=False)
    phone = PhoneNumberField(unique=True, null=False, blank=False)
    location = models.PointField(null=False, blank=False)
    maxTravelDist = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False, blank=False)
    address = models.CharField(max_length=128, null=False, blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    details = models.CharField(max_length=128, null=True, blank=True)
    participants = models.ManyToManyField(Patient, related_name='events')

    def __str__(self):
        return self.name