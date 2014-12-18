# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('profile', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='teachers')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
