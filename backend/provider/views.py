from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import Patient, IncidentType, Incident, Event
from .serializers import PatientSerializer, IncidentTypeSerializer, IncidentSerializer, EventSerializer
from django.shortcuts import render

class IncidentTypeList(ListCreateAPIView):
    queryset = IncidentType.objects.all().order_by('name')
    serializer_class = IncidentTypeSerializer

class IncidentTypeDetail(RetrieveUpdateDestroyAPIView):
    queryset = IncidentType.objects.all()
    serializer_class = IncidentTypeSerializer

class IncidentList(ListCreateAPIView):
    # queryset = Incident.objects.all().order_by('id')
    serializer_class = IncidentSerializer

    def get_queryset(self):
        queryset = Incident.objects.all()
        treatment = self.request.query_params.get('treatment', None)
        in_month = self.request.query_params.get('month', None)
        if treatment is not None and in_month is not None:
            if int(in_month) == 0:
                queryset.filter(type__name='treatment')
            elif int(in_month) > 0 and int(in_month) < 13:
                int_month = int(in_month)
                queryset.filter(type__name='treatment').filter(month='int_month')
        return queryset

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
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save()

class EventDetail(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

def handlePatient(request):
    return render(request, 'patient.html')

def handleProvider(request):
    return render(request, 'provider.html')

def handleIndex(request):
    return render(request, 'index.html')