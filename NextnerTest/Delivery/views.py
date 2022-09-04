from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Delivery, Address
from .forms import DeliveryForm, AddressForm, address_formset


class ListItemsView(ListView):
    model = Delivery
    template_name = 'Delivery/index.html'
    context_object_name = 'delivery'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListItemsView, self).get_context_data(**kwargs)
        context['title'] = 'Список доставок'
        return context


# def index(request):
#     delivery = Delivery.objects.all()
#     context = {
#         'delivery': delivery,
#         'title': 'Список товаров',
#     }
#     return render(request, 'Delivery/index.html', context)


def add_delivery(request):
    context = {'title': 'Список товаров', }
    addresses_count = 10
    if request.method == 'POST':
        form_delivery = DeliveryForm(request.POST, request.FILES)
        forms_address = address_formset(addresses_count)(request.POST)
        if form_delivery.is_valid() and forms_address.is_valid():
            b = form_delivery.save()
            for form in forms_address:
                a = form.save()
                b.address_delivery.add(a)
            return redirect('home')
    else:
        form_delivery = DeliveryForm()
        forms_address = address_formset(addresses_count)(queryset=Address.objects.none())
        context['form_delivery'] = form_delivery
        context['form_address'] = forms_address
    return render(request, 'Delivery/add_delivery.html', context)

