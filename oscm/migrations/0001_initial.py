# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('userName', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=40)),
                ('role', models.CharField(max_length=40, choices=[(b'Admin', b'Admin'), (b'SuperUser', b'Super User'), (b'User', b'User')])),
                ('lastLogin', models.DateTimeField()),
            ],
        ),
    ]
