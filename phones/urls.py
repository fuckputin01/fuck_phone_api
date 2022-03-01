from django.urls import path
from .views import phone_list, phone_detail
#
urlpatterns = [
    path('phones', phone_list, name='list_phones'),
    path('phones/<int:phone_number>', phone_detail, name='update_phone'),
]
