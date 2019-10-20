"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from provider.views import IncidentTypeList, IncidentTypeDetail, IncidentList, IncidentDetail
from provider.views import PatientList, PatientDetail, EventList, EventDetail
from provider.views import handleIndex, handlePatient, handleProvider
from sms.views import sms_response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', PatientList.as_view()),
    path('patients/<int:pk>/', PatientDetail.as_view()),
    path('incidents/', IncidentList.as_view()),
    path('incidents/<int:pk>/', IncidentDetail.as_view()),
    path('itypes/', IncidentTypeList.as_view()),
    path('itypes/<int:pk>/', IncidentTypeDetail.as_view()),
    path('events/', EventList.as_view()),
    path('events/<int:pk>/', EventDetail.as_view()),
    path('sms/', sms_response),
    path('', handleIndex),
    path('index.html', handleIndex),
    path('provider.html', handleProvider),
    path('patient.html', handlePatient)
]
