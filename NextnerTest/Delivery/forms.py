from django import forms
from django.forms import modelformset_factory

from .models import Delivery, Address


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['id', 'item_name', 'type_item', 'delivery_date', 'file']
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'type_item': forms.Select(attrs={'class': 'form-control'}),
            'delivery_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'})
        }


def address_formset(extra):
    address_form_set = modelformset_factory(Address, form=AddressForm, extra=extra)
    return address_form_set

