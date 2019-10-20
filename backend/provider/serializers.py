from rest_framework import serializers
from . import models

# class InstanceTypeSerializer(serializers.ModelSerializer):
#     """ ... """
#     class Meta:
#         model = models.InstanceType
#         fields = ("id", "name",)

# class InstanceTimeSerializer(serializers.ModelSerializer):
#     id = serializers.Field(source='instance_type.id')
#     name = serializers.Field(source='instance_type.name')

#     class Meta:
#         model = models.InstanceTime
#         fields = ('id', 'name', 'month',)

# class InstanceSerializer(serializers.ModelSerializer):
#     """ ... """
#     occurences = InstanceTimeSerializer(source='instances', many=True)

#     class Meta:
#         model = models.Instance
#         fields = ("id", "location", "occurrences",)

class IncidentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IncidentType
        fields = ('id', 'name',)

class IncidentSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=models.IncidentType.objects.all()
    )
    class Meta:
        model = models.Incident
        fields = ('id', 'type', 'month', 'location',)

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = ('id', 'name', 'phone', 'location', 'maxTravelDist',)

class EventSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=models.Patient.objects.all(),
        allow_null=True
    )

    class Meta:
        model = models.Event
        fields = ('id', 'name', 'address', 'time', 'details', 'participants',)
