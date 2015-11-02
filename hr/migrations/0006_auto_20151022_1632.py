# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0005_auto_20151022_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='user_position',
            field=models.CharField(max_length=10, verbose_name=b'\xe8\x81\x8c\xe4\xbd\x8d', choices=[(b'SD', b'\xe6\xa0\xa1\xe9\x95\xbf'), (b'ASD', b'\xe5\x8a\xa9\xe7\x90\x86\xe6\xa0\xa1\xe9\x95\xbf'), (b'DOS', b'\xe6\x95\x99\xe5\xad\xa6\xe5\x89\xaf\xe6\xa0\xa1\xe9\x95\xbf'), (b'CCM', b'\xe5\x92\xa8\xe8\xaf\xa2\xe7\xbb\x8f\xe7\x90\x86'), (b'CRM', b'\xe5\xae\xa2\xe6\x9c\x8d\xe7\xbb\x8f\xe7\x90\x86'), (b'CCS', b'\xe5\x92\xa8\xe8\xaf\xa2\xe4\xb8\xbb\xe7\xae\xa1'), (b'CRS', b'\xe5\xae\xa2\xe6\x9c\x8d\xe4\xb8\xbb\xe7\xae\xa1'), (b'TRM', b'\xe5\xad\xa6\xe7\xa7\x91\xe7\xbb\x84\xe9\x95\xbf'), (b'TRS', b'\xe5\xad\xa6\xe7\xa7\x91\xe5\xb8\xa6\xe5\xa4\xb4\xe4\xba\xba'), (b'CC', b'\xe6\x95\x99\xe8\x82\xb2\xe9\xa1\xbe\xe9\x97\xae'), (b'CR', b'\xe7\x8f\xad\xe4\xb8\xbb\xe4\xbb\xbb'), (b'TR', b'\xe5\xad\xa6\xe7\xa7\x91\xe6\x95\x99\xe5\xb8\x88'), (b'YWTR', b'\xe8\xaf\xad\xe6\x96\x87\xe6\x95\x99\xe5\xb8\x88'), (b'SXTR', b'\xe6\x95\xb0\xe5\xad\xa6\xe6\x95\x99\xe5\xb8\x88'), (b'YYTR', b'\xe8\x8b\xb1\xe8\xaf\xad\xe6\x95\x99\xe5\xb8\x88'), (b'WLTR', b'\xe7\x89\xa9\xe7\x90\x86\xe6\x95\x99\xe5\xb8\x88'), (b'HXTR', b'\xe5\x8c\x96\xe5\xad\xa6\xe6\x95\x99\xe5\xb8\x88'), (b'KXTR', b'\xe7\xa7\x91\xe5\xad\xa6\xe6\x95\x99\xe5\xb8\x88'), (b'ZSDTR', b'\xe6\x94\xbf\xe5\x8f\xb2\xe5\x9c\xb0\xe6\x95\x99\xe5\xb8\x88'), (b'QTTR', b'\xe5\x85\xb6\xe4\xbb\x96\xe6\x95\x99\xe5\xb8\x88'), (b'TL', b'\xe5\x87\xba\xe7\xba\xb3'), (b'CP', b'\xe6\x95\x99\xe5\x8a\xa1\xe4\xb8\x93\xe5\x91\x98'), (b'AD', b'\xe8\xa1\x8c\xe6\x94\xbf'), (b'CL', b'\xe4\xbf\x9d\xe6\xb4\x81')]),
        ),
    ]
