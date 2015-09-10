# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DecorationContract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Proj_Name', models.CharField(max_length=100, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('sign_date', models.DateField(verbose_name=b'\xe7\xad\xbe\xe7\xba\xa6\xe6\x97\xa5\xe6\x9c\x9f')),
                ('price', models.IntegerField(default=0, verbose_name=b'\xe5\x90\x88\xe7\xba\xa6\xe6\x80\xbb\xe4\xbb\xb7')),
                ('first_payment', models.IntegerField(default=0, verbose_name=b'\xe9\xa6\x96\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98')),
                ('Sec_payment', models.IntegerField(default=0, verbose_name=b'\xe4\xba\x8c\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98')),
                ('Thrd_payment', models.IntegerField(default=0, verbose_name=b'\xe4\xb8\x89\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98')),
                ('Fourth_payment', models.IntegerField(default=0, verbose_name=b'\xe5\x9b\x9b\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98')),
                ('Fifth_payment', models.IntegerField(default=0, verbose_name=b'\xe4\xba\x94\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98')),
            ],
            options={
                'verbose_name': '\u88c5\u4fee\u5de5\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Proj_name', models.CharField(max_length=100, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('adr_txt', models.CharField(max_length=100, verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80')),
                ('sign_date', models.DateField(verbose_name=b'\xe7\xad\xbe\xe7\xba\xa6\xe6\x97\xa5\xe6\x9c\x9f')),
                ('rent', models.IntegerField(default=0, verbose_name=b'\xe7\xa7\x9f\xe9\x87\x91')),
                ('landlord', models.CharField(max_length=100, verbose_name=b'\xe6\x88\xbf\xe4\xb8\x9c\xe5\x90\x8d\xe7\xa7\xb0')),
                ('landlord_account', models.BigIntegerField(verbose_name=b'\xe6\x88\xbf\xe4\xb8\x9c\xe8\xb4\xa6\xe5\x8f\xb7')),
                ('landlord_account_bank', models.CharField(max_length=200, verbose_name=b'\xe5\xbc\x80\xe6\x88\xb7\xe8\xa1\x8c')),
                ('payment_period', models.CharField(max_length=50, verbose_name=b'\xe6\x94\xaf\xe4\xbb\x98\xe5\x91\xa8\xe6\x9c\x9f')),
                ('deposit', models.IntegerField(default=0, verbose_name=b'\xe7\xa7\x9f\xe8\xb5\x81\xe4\xbf\x9d\xe8\xaf\x81\xe9\x87\x91')),
            ],
            options={
                'verbose_name': '\u6821\u533a\u9879\u76ee',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supplier_name', models.CharField(max_length=100, verbose_name=b'\xe4\xbe\x9b\xe5\xba\x94\xe5\x95\x86\xe5\x90\x8d\xe7\xa7\xb0')),
                ('supplier_account', models.BigIntegerField(verbose_name=b'\xe4\xbe\x9b\xe5\xba\x94\xe5\x95\x86\xe8\xb4\xa6\xe5\x8f\xb7')),
                ('supplier_account_bank', models.CharField(max_length=200, verbose_name=b'\xe5\xbc\x80\xe6\x88\xb7\xe8\xa1\x8c')),
            ],
            options={
                'verbose_name': '\u4f9b\u5e94\u5546',
            },
        ),
        migrations.CreateModel(
            name='SupplierType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supplier_Type', models.CharField(max_length=50, verbose_name=b'\xe4\xbe\x9b\xe5\xba\x94\xe5\x95\x86\xe7\xb1\xbb\xe5\x9e\x8b')),
            ],
            options={
                'verbose_name': '\u4f9b\u5e94\u5546\u7c7b\u578b',
            },
        ),
        migrations.AddField(
            model_name='supplier',
            name='supplier_Type',
            field=models.ForeignKey(to='OA.SupplierType'),
        ),
        migrations.AddField(
            model_name='decorationcontract',
            name='proj_type',
            field=models.ForeignKey(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\xb1\xbb\xe5\x88\xab', to='OA.SupplierType'),
        ),
        migrations.AddField(
            model_name='decorationcontract',
            name='project_name',
            field=models.ForeignKey(to='OA.Project'),
        ),
        migrations.AddField(
            model_name='decorationcontract',
            name='supplier',
            field=models.ForeignKey(verbose_name=b'\xe4\xbe\x9b\xe5\xba\x94\xe5\x95\x86', to='OA.Supplier'),
        ),
    ]
