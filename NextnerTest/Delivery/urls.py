from django.urls import path
from Delivery.views import *

urlpatterns = [
    path('', ListItemsView.as_view(), name='home'),
    path('add_delivery', add_delivery, name='add_delivery')
]