from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import Patient, IncidentType, Incident, Event
from .serializers import PatientSerializer, IncidentTypeSerializer, IncidentSerializer, EventSerializer
from django.shortcuts import render
from django.contrib.gis.db.models.functions import Distance
from django.db.models import F
from twilio.rest import TwilioRestClient
from django.conf import settings

# def send_sms(to, message):
#     client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#     response = client.messages.create(body=message, to=to, from_=settings.TWILIO_PHONE_NO)
#     return response

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

    # def perform_create(self, serializer):
        
    #     client = Client(account_sid, auth_token)

    #     p = self.request.location
    #     new_queryset = Patient.objects.annotate(
    #         distance=Distance('location', p)).filter(distance__lte=F('maxTravelDist')
    #     )
    #     for patient in new_queryset:
    #         print(patient.)
    #     serializer.save()

class EventDetail(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

def handlePatient(request):
    return render(request, 'patient.html')

def handleProvider(request):
    return render(request, 'provider.html')

def handleIndex(request):
    return render(request, 'index.html')