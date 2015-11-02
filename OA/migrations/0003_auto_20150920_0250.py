# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OA', '0002_auto_20150907_0132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='decorationcontract',
            options={'verbose_name_plural': '\u88c5\u4fee\u5de5\u7a0b\u5217\u8868'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name_plural': '\u6821\u533a\u5217\u8868'},
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={'verbose_name_plural': '\u4f9b\u5e94\u5546\u4fe1\u606f'},
        ),
        migrations.AlterModelOptions(
            name='suppliertype',
            options={'verbose_name_plural': '\u4f9b\u5e94\u5546\u7c7b\u578b'},
        ),
    ]
