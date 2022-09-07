from django import forms
from django.forms import modelformset_factory, BaseModelFormSet

from .models import Delivery, Address


class DeliveryForm(forms.ModelForm):
    address_delivery = forms.ModelChoiceField(queryset=Address.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Delivery
        fields = ['item_name', 'type_item', 'delivery_date', 'file', 'address_delivery']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'type_item': forms.Select(attrs={'class': 'form-control'}),
            'delivery_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['address_delivery'].empty_label = None


class BaseDeliveryFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = Address.objects.none()


DeliveryFormSet = modelformset_factory(
    Delivery,
    formset=BaseDeliveryFormSet,
    fields=('item_name', 'type_item', 'delivery_date', 'file', 'address_delivery'),
    form=DeliveryForm,
    extra=2,
    max_num=10,
    min_num=0
)


# class AddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields = ['address']
#         widgets = {
#             'address': forms.TextInput(attrs={'class': 'form-control'})
#         }
#
#
# class BaseAddressFormSet(BaseModelFormSet):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.queryset = Address.objects.none()
#
#
# AddressFormSet = modelformset_factory(
#     Address,
#     formset=BaseAddressFormSet,
#     fields=('address',),
#     form=AddressForm,
#     extra=10,
#     max_num=10,
#     min_num=0
# )


# def address_formset(extra):
#     address_form_set = modelformset_factory(Address, form=AddressForm, extra=extra)
#     return address_form_set

