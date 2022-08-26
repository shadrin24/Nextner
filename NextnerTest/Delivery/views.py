from django.shortcuts import render, redirect

from .models import Delivery
from .forms import DeliveryForm


def index(request):
    delivery = Delivery.objects.all()
    context = {
        'delivery': delivery,
        'title': 'Список товаров',
    }
    return render(request, 'Delivery/index.html', context)


def add_delivery(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            print('post')
            delivery = form.save()
            return redirect(delivery)
    else:
        form = DeliveryForm()
    context = {
        'title': 'Список товаров',
        'form': form,
    }
    return render(request, 'Delivery/add_delivery.html', context)
