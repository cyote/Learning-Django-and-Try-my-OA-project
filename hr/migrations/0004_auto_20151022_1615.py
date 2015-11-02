# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_auto_20151022_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='user_workcode',
            field=models.CharField(default=0, unique=True, max_length=12, verbose_name=b'\xe5\xb7\xa5\xe5\x8f\xb7'),
        ),
    ]
