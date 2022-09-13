from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, FormView
from .models import Delivery, Address
from .forms import DeliveryForm, AddressForm, AddressFormSet


class ListItemsView(ListView):
    model = Delivery
    template_name = 'Delivery/index.html'
    context_object_name = 'delivery'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListItemsView, self).get_context_data(**kwargs)
        context['title'] = 'Список доставок'
        return context


class AddDelivery(CreateView):
    model = Delivery
    form_class = DeliveryForm
    template_name = 'Delivery/add_delivery.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(AddDelivery, self).get_context_data(**kwargs)
        context['formset'] = AddressFormSet()
        # context['delivery_form'] = DeliveryForm()
        return context

    def post(self, request, *args, **kwargs):
        formset = AddressFormSet(request.POST)
        delivery_form = DeliveryForm(request.POST, request.FILES)
        if formset.is_valid() and delivery_form.is_valid():
            return self.form_valid(formset, delivery_form)
        else:
            return HttpResponseRedirect('/error')

    def form_valid(self, formset, delivery_form):
        delivery = delivery_form.save()
        for form in formset:
            if form.cleaned_data:
                address = form.cleaned_data['address_delivery']
                delivery.address_delivery.add(address)
        return HttpResponseRedirect('/')