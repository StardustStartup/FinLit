from rest_framework import serializers
from . import models

class InstanceTypeSerializer(serializers.ModelSerializer):
    """ ... """
    class Meta:
        model = models.InstanceType
        fields = ("id", "name",)

class InstanceSerializer(serializers.ModelSerializer):
    """ ... """
    category = serializers.PrimaryKeyRelatedField(
        queryset=models.InstanceType.objects.all()
    )
    class Meta:
        model = models.Instance
        fields = ("id", "month", "location", "type",)
        depth = 1