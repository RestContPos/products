# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0003_auto_20150914_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(default=b'', max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(default=b'', max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('sell_price', models.DecimalField(default=0.0, max_digits=19, decimal_places=2)),
                ('buy_price', models.DecimalField(default=0.0, max_digits=19, decimal_places=2)),
                ('category', models.ForeignKey(default=1, to='products.Category')),
                ('provider', models.ForeignKey(default=1, to='providers.Provider')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
