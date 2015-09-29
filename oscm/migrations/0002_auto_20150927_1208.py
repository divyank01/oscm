# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oscm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userName', models.CharField(max_length=40)),
                ('pwd', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='signup',
            name='role',
            field=models.CharField(default='null', max_length=40, choices=[(b'admin', b'Admin'), (b's_user', b'Super User'), (b'user', b'User')]),
            preserve_default=False,
        ),
    ]
