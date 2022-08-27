from django import forms
from .models import Delivery


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['item_name', 'type_item', 'delivery_date', 'file', 'address_delivery']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'type_item': forms.Select(attrs={'class': 'form-control'}),
            'delivery_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'address_delivery': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

