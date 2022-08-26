# Generated by Django 4.1 on 2022-08-26 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(db_index=True, max_length=150, verbose_name='Тип товара')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адресы',
                'ordering': ['address'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(db_index=True, max_length=150, verbose_name='Тип товара')),
            ],
            options={
                'verbose_name': 'Тип товара',
                'verbose_name_plural': 'Типы товаров',
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.TextField(verbose_name='Название товара')),
                ('delivery_date', models.DateField(verbose_name='Дата доставки')),
                ('file', models.FileField(upload_to='', verbose_name='Файл')),
                ('address_delivery', models.ManyToManyField(to='Delivery.address')),
                ('type_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Delivery.type')),
            ],
            options={
                'verbose_name': 'Доставка товара',
                'verbose_name_plural': 'Доставки товара',
                'ordering': ['delivery_date'],
            },
        ),
    ]