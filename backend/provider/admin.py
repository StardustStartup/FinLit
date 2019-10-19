from django.contrib import admin
from .models import Instance, InstanceType

admin.site.register(Instance)
admin.site.register(InstanceType)