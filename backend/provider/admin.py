from django.contrib import admin
from .models import IncidentType, Incident, Patient, Event

admin.site.register(IncidentType)
admin.site.register(Incident)
admin.site.register(Patient)
admin.site.register(Event)