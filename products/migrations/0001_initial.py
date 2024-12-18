# Generated by Django 5.1.2 on 2024-10-30 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=3, verbose_name='Currency')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Title')),
                ('quantity', models.PositiveIntegerField()),
                ('barcode', models.CharField(max_length=13, verbose_name='Barcode')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productprice', verbose_name='Price')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.producttype', verbose_name='Type')),
            ],
        ),
    ]
