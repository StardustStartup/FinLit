from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import Patient
from .serializers import PatientSerializer

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

class PatientList(ListCreateAPIView):
    queryset = Patient.objects.all().order_by('id')
    serializer_class = PatientSerializer

class PatientDetail(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    