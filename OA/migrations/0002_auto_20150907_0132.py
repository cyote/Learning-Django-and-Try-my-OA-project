# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OA', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decorationcontract',
            name='project_name',
            field=models.ForeignKey(verbose_name=b'\xe6\xa0\xa1\xe5\x8c\xba', to='OA.Project'),
        ),
    ]
