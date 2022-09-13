from django import forms
from django.forms import modelformset_factory, BaseModelFormSet, formset_factory

from .models import Delivery, Address, Type


class DeliveryForm(forms.ModelForm):

    class Meta:
        model = Delivery
        fields = ['item_name', 'type_item', 'delivery_date', 'file'
                  ]
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'type_item': forms.Select(attrs={'class': 'form-control'}),
            'delivery_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }


class AddressForm(forms.Form):
    address_delivery = forms.ModelChoiceField(queryset=Address.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), label='Адрес доставки')


AddressFormSet = formset_factory(AddressForm, extra=6)


