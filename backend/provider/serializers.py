from rest_framework import serializers
from . import models

class InstanceTypeSerializer(serializers.ModelSerializer):
    """ ... """
    class Meta:
        model = models.InstanceType
        fields = ("id", "name",)

class InstanceTimeSerializer(serializers.ModelSerializer):
    id = serializers.Field(source='instance_type.id')
    name = serializers.Field(source='instance_type.name')

    class Meta:
        model = models.InstanceTime
        fields = ('id', 'name', 'month',)

class InstanceSerializer(serializers.ModelSerializer):
    """ ... """
    occurences = InstanceTimeSerializer(source='instances', many=True)

    class Meta:
        model = models.Instance
        fields = ("id", "location", "occurrences",)
