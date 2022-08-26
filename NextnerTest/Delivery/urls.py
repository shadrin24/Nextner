from django.urls import path
from Delivery.views import index, test2

urlpatterns = [
    path('', index),
]