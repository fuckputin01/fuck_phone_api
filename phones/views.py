from datetime import datetime
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Phone
from .serializers import PhoneSerializer
import random

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.order_by('last_used').all()
    serializer_class = PhoneSerializer

    def get_queryset(self):
        l = list(self.queryset[:500])
        random.shuffle(l)
        return l

    def update_last_used(self, request, *args, **kwargs):
        instance: Phone = get_object_or_404(Phone, phone_int=kwargs['phone_number'])
        instance.last_used = datetime.now()
        instance.save(update_fields=['last_used'])
        return Response({'ok':True})

    def update_has_whatsapp(self, request, *args, **kwargs):
        instance: Phone = get_object_or_404(Phone, phone_int=kwargs['phone_number'])
        instance.has_whatsapp = True
        instance.save(update_fields=['has_whatsapp'])
        return Response({'ok':True})


phone_list = PhoneViewSet.as_view({'get': 'list', 'post': 'create'})
phone_detail = PhoneViewSet.as_view({'put': 'update_last_used', 'post': 'update_has_whatsapp'})
