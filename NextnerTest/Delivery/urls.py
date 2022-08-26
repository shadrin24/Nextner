from django.urls import path
from Delivery.views import index, add_delivery

urlpatterns = [
    path('', index, name='home'),
    path('add_delivery', add_delivery, name='add_delivery')
]