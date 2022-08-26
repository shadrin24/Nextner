from django.urls import path
from Delivery.views import index

urlpatterns = [
    path('', index),
]