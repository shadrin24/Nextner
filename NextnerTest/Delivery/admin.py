from django.contrib import admin

from .models import Delivery, Address, Type


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'type_item', 'delivery_date', 'file',)
    list_display_links = ('id', 'item_name')
    search_fields = ('item_name',)
    list_editable = ('type_item', 'delivery_date')


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type',)
    list_display_links = ('id', 'type')
    search_fields = ('type',)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'address',)
    list_display_links = ('id', 'address')
    search_fields = ('address',)


admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Type)
admin.site.register(Address)

