from django.db import models


class Delivery(models.Model):
    item_name = models.TextField(verbose_name='Название товара')
    type_item = models.ForeignKey('Type', on_delete=models.PROTECT, verbose_name='Тип товара')
    delivery_date = models.DateField(verbose_name='Дата доставки')
    file = models.FileField(verbose_name='Файл')
    address_delivery = models.ManyToManyField('Address', verbose_name='Адрес доставки')

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name = 'Доставка товара'
        verbose_name_plural = 'Доставки товара'
        ordering = ['delivery_date']


class Type(models.Model):
    type = models.CharField(max_length=150, db_index=True, verbose_name='Тип товара')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'
        ordering = ['type']


class Address(models.Model):
    address = models.CharField(max_length=150, db_index=True, verbose_name='Адрес')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адресы'
        ordering = ['address']
