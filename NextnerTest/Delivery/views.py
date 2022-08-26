from django.shortcuts import render
from django.http import HttpResponse

from .models import Delivery


def index(request):
    delivery = Delivery.objects.all()
    context = {
        'delivery': delivery,
        'title': 'Список товаров',
    }
    return render(request, 'Delivery/index.html', context)
