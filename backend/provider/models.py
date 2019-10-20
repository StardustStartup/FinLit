from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

# class InstanceType(models.Model):
#     """ Refers to an illness/disease or category thereof. """
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=128, null=False, blank=False)

#     class Meta:
#         ordering = ("name",)

#     def __str__(self):
#         return self.name

# class Instance(models.Model):
#     """ Refers to patient, which may hold references to multiple InstanceTypes. """
#     id = models.AutoField(primary_key=True)
#     location = models.PointField(null=False, blank=False)
#     occurrences = models.ManyToManyField(InstanceType, related_name='instances', through='InstanceTime')

#     class Meta:
#         ordering = ("id",)

#     def __str__(self):
#         return str(self.id)

# class InstanceTime(models.Model):
#     instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
#     instance_type = models.ForeignKey(InstanceType, on_delete=models.CASCADE)
#     month = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(12)])

#     class Meta:
#         ordering = ("month",)

#     def __str__(self):
#         return str(self.month)

class IncidentType(models.Model):
    pass

class Incident(models.Model):
    pass

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False, blank=False)
    phone = PhoneNumberField(unique=True, null=False, blank=False)
    location = models.PointField(null=False, blank=False)
    maxTravelDist = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(100)])

class Event(models.Model):
    pass
