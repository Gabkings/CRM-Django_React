# Generated by Django 3.0.8 on 2020-08-04 21:11

import clients.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchaser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('image', models.ImageField(default='default.png', upload_to='customer_photos/%Y/%m/%d/')),
                ('data_added', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='purchaserShippingDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequent_customer', models.BooleanField(default=False)),
                ('owner', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=12)),
                ('zip_code', models.CharField(blank=True, max_length=12)),
                ('description', models.TextField(blank=True)),
                ('county', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Mombasa', 'Mombasa'), ('Kisumu', 'Kisumu'), ('Machakos', 'Machakos'), ('Kiambu', 'Kiambu')], default='Nairobi', max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('country', models.CharField(choices=[('Kenya', 'Kenya')], default='Kenya', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='paymentInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceNo', models.CharField(default=clients.models.increment_invoice_number, max_length=50, unique=True)),
                ('product', models.CharField(blank=True, max_length=50)),
                ('mode', models.CharField(choices=[('Mpesa', 'Mpesa'), ('Bank', 'Bank'), ('Cheque', 'Cheque'), ('Cash', 'Cash')], default='Mpesa', max_length=20)),
                ('date', models.DateField(default=datetime.date.today)),
                ('quantity', models.PositiveSmallIntegerField(blank=True, default=1)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Delivered', 'Delivered')], default='Pending', max_length=20)),
                ('payment_made', models.IntegerField(default=0)),
                ('invoiceOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_detail', to='clients.Purchaser')),
            ],
        ),
    ]
