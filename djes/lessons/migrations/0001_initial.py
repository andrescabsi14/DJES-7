# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='lessons')),
                ('lesson_file', models.FileField(upload_to='lessons')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
