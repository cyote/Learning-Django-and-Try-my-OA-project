# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_auto_20151022_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='user_workcode',
            field=models.CharField(primary_key=True, default=0, serialize=False, max_length=12, unique=True, verbose_name=b'\xe5\xb7\xa5\xe5\x8f\xb7'),
        ),
    ]
