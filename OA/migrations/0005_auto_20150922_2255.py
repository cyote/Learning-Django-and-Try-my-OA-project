# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OA', '0004_auto_20150920_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='supplier_Type',
            field=models.ForeignKey(verbose_name=b'\xe4\xbe\x9b\xe5\xba\x94\xe5\x95\x86\xe7\xb1\xbb\xe5\x9e\x8b', to='OA.SupplierType'),
        ),
    ]
