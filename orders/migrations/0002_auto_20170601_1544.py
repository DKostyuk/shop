# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 12:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'ProductInOrder', 'verbose_name_plural': 'ProductInOrders'},
        ),
    ]
