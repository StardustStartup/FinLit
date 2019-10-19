from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import InstanceType, Instance
from .serializers import InstanceTypeSerializer, InstanceSerializer

class InstanceList(ListCreateAPIView):
    # add permissions later
    queryset = Instance.objects.all().order_by("id")
    serializer_class = InstanceSerializer

class InstanceDetail(RetrieveUpdateDestroyAPIView):
    # add permissions later
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer

class InstanceTypeList(ListAPIView):
    queryset = InstanceType.objects.all().order_by("name")
    serializer_class = InstanceTypeSerializer

class InstanceTypeDetail(RetrieveAPIView):
    queryset = InstanceType.objects.all()
    serializer_class = InstanceTypeSerializer