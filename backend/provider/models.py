from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class InstanceType(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length= 128, null = False, blank = False)

class Instance(models.Model):
    id = models.AutoField(primary_key = True)
    month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    location = models.PointField(null = False, blank = False)
    type = models.ForeignKey(InstanceType, on_delete = models.CASCADE)