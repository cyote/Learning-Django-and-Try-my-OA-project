# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='decorationcontract',
            name='Proj_Name',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='decorationcontract',
            name='project',
            field=models.ForeignKey(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\x89\x80\xe5\xb1\x9e\xe6\xa0\xa1\xe5\x8c\xba', to='polls.Project'),
        ),
    ]
