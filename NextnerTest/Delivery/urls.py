from django.urls import path
from Delivery.views import *

urlpatterns = [
    path('', ListItemsView.as_view(), name='home'),
    path('add_delivery', AddDelivery.as_view(), name='add_delivery')
]