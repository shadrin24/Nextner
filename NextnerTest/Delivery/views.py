from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

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
    context = {'title': 'Список товаров', }
    if request.method == 'POST' and request.FILES:
        print(request.FILES)
        form = DeliveryForm(request.POST, request.FILES)
        if form.is_valid():
            print('post')
            form.save()
            return redirect('home')
    else:
        form = DeliveryForm()
        context['form'] = form
    return render(request, 'Delivery/add_delivery.html', context)

