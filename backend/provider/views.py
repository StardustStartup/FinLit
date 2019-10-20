from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import Patient, IncidentType, Incident
from .serializers import PatientSerializer, IncidentTypeSerializer, IncidentSerializer

# class PatientList(ListCreateAPIView):
#     # add permissions later
#     queryset = Instance.objects.all().order_by("id")
#     serializer_class = InstanceSerializer

# class PatientDetail(RetrieveUpdateDestroyAPIView):
#     # add permissions later
#     queryset = Instance.objects.all()
#     serializer_class = InstanceSerializer

# class InstanceList(ListAPIView):
#     queryset = 

# class InstanceTypeList(ListAPIView):
#     queryset = InstanceType.objects.all().order_by("name")
#     serializer_class = InstanceTypeSerializer

# class InstanceTypeDetail(RetrieveAPIView):
#     queryset = InstanceType.objects.all()
#     serializer_class = InstanceTypeSerializer

class IncidentTypeList(ListCreateAPIView):
    queryset = IncidentType.objects.all().order_by('name')
    serializer_class = IncidentTypeSerializer

class IncidentTypeDetail(RetrieveUpdateDestroyAPIView):
    queryset = IncidentType.objects.all()
    serializer_class = IncidentTypeSerializer

class IncidentList(ListCreateAPIView):
    queryset = Incident.objects.all().order_by('id')
    serializer_class = IncidentSerializer

class IncidentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class PatientList(ListCreateAPIView):
    queryset = Patient.objects.all().order_by('id')
    serializer_class = PatientSerializer

class PatientDetail(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class EventList(ListCreateAPIView):
    pass

class EventDetail(RetrieveUpdateDestroyAPIView):
    pass
