from django.contrib import admin
from .models import Phone

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('phone_int', 'last_used','note')

admin.site.register(Phone, PhoneAdmin)
