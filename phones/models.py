from django.db import models
from datetime import datetime

class Phone(models.Model):
    phone_int = models.BigIntegerField(unique=True)
    last_used = models.DateTimeField(default=datetime.strptime('Feb 24 2022', '%b %d %Y'))
    note = models.TextField(blank=True, default='')
    has_whatsapp = models.BooleanField(default=False)
    name = models.CharField(max_length=64, default='')
