from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .models import Delivery, Address
from .forms import DeliveryForm, AddressForm


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
        form_delivery = DeliveryForm(request.POST, request.FILES)
        form_address = AddressForm(request.POST)
        if form_delivery.is_valid() and form_address.is_valid():
            a = form_address.save()
            b = form_delivery.save()
            b.address_delivery.add(a)
            return redirect('home')
    elif request.method == 'POST':
        form_delivery = DeliveryForm(request.POST)
        form_address = AddressForm(request.POST)
        if form_delivery.is_valid() and form_address.is_valid():
            a = form_address.save()
            b = form_delivery.save()
            b.address_delivery.add(a)
            return redirect('home')
    else:
        form_delivery = DeliveryForm()
        form_address = AddressForm()
        context['form_delivery'] = form_delivery
        context['form_address'] = form_address
    return render(request, 'Delivery/add_delivery.html', context)


# def add_address(request):
#     context = {}
#     if request.method == 'POST':
#         form = AddressForm(request.POST)
#         if form.is_valid():
#             print('post')
#             form.save()
#             return redirect('home')
#     else:
#         form = AddressForm()
#         context['form'] = form
#     return render(request, 'Delivery/add_delivery.html', context)
