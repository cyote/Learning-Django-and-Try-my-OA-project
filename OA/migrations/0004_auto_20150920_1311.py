# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('OA', '0003_auto_20150920_0250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='decorationcontract',
            old_name='Fifth_payment',
            new_name='fif_payment',
        ),
        migrations.RenameField(
            model_name='decorationcontract',
            old_name='Fourth_payment',
            new_name='fou_payment',
        ),
        migrations.RenameField(
            model_name='decorationcontract',
            old_name='project_name',
            new_name='school_name',
        ),
        migrations.RenameField(
            model_name='decorationcontract',
            old_name='Sec_payment',
            new_name='sec_payment',
        ),
        migrations.RenameField(
            model_name='decorationcontract',
            old_name='Thrd_payment',
            new_name='thd_payment',
        ),
        migrations.RemoveField(
            model_name='decorationcontract',
            name='Proj_Name',
        ),
        migrations.AddField(
            model_name='decorationcontract',
            name='fif_payment_date',
            field=models.DateField(null=True, verbose_name=b'\xe4\xba\x94\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AddField(
            model_name='decorationcontract',
            name='first_payment_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 5, 9, 25, 101306, tzinfo=utc), verbose_name=b'\xe9\xa6\x96\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='decorationcontract',
            name='fou_payment_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 5, 9, 37, 360414, tzinfo=utc), verbose_name=b'\xe5\x9b\x9b\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='decorationcontract',
            name='proj_name',
            field=models.CharField(default=datetime.datetime(2015, 9, 20, 5, 9, 45, 112135, tzinfo=utc), max_length=20, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='decorationcontract',
            name='sec_payment_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 5, 9, 53, 816197, tzinfo=utc), verbose_name=b'\xe4\xba\x8c\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='decorationcontract',
            name='thd_payment_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 5, 10, 2, 960118, tzinfo=utc), verbose_name=b'\xe4\xb8\x89\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='eit_pay',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x85\xab\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98'),
        ),
        migrations.AddField(
            model_name='project',
            name='eit_pay_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 5, 10, 16, 325455, tzinfo=utc), verbose_name=b'\xe5\x85\xab\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='fif_pay',
            field=models.IntegerField(default=0, verbose_name=b'\xe4\xba\x94\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98'),
        ),
        migrations.AddField(
            model_name='project',
            name='fif_pay_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 5, 10, 23, 962563, tzinfo=utc), verbose_name=b'\xe4\xba\x94\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='first_pay',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\xa6\x96\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98'),
        ),
        migrations.AddField(
            model_name='project',
            name='first_pay_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 5, 10, 32, 522197, tzinfo=utc), verbose_name=b'\xe9\xa6\x96\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='fou_pay',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x9b\x9b\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98'),
        ),
        migrations.AddField(
            model_name='project',
            name='fou_pay_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 5, 10, 56, 447657, tzinfo=utc), verbose_name=b'\xe5\x9b\x9b\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='nin_pay',
            field=models.IntegerField(default=0, verbose_name=b'\xe4\xb9\x9d\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98'),
        ),
        migrations.AddField(
            model_name='project',
            name='nin_pay_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 5, 11, 6, 329289, tzinfo=utc), verbose_name=b'\xe4\xb9\x9d\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='proj_code',
            field=models.CharField(default=1, max_length=3, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\xbc\x96\xe5\x8f\xb7'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='sec_pay',
            field=models.IntegerField(default=0, verbose_name=b'\xe4\xba\x8c\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98'),
        ),
        migrations.AddField(
            model_name='project',
            name='sec_pay_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 5, 11, 24, 392322, tzinfo=utc), verbose_name=b'\xe4\xba\x8c\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='sev_pay',
            field=models.IntegerField(default=0, verbose_name=b'\xe4\xb8\x83\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98'),
        ),
        migrations.AddField(
            model_name='project',
            name='sev_pay_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 5, 11, 36, 165437, tzinfo=utc), verbose_name=b'\xe4\xb8\x83\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='six_pay',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x85\xad\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98'),
        ),
        migrations.AddField(
            model_name='project',
            name='six_pay_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 5, 11, 43, 140598, tzinfo=utc), verbose_name=b'\xe5\x85\xad\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='ten_pay',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x8d\x81\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98'),
        ),
        migrations.AddField(
            model_name='project',
            name='ten_pay_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 5, 11, 49, 508186, tzinfo=utc), verbose_name=b'\xe5\x8d\x81\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='thd_pay',
            field=models.IntegerField(default=0, verbose_name=b'\xe4\xb8\x89\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98'),
        ),
        migrations.AddField(
            model_name='project',
            name='thd_pay_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 5, 11, 56, 660095, tzinfo=utc), verbose_name=b'\xe4\xb8\x89\xe6\x9c\x9f\xe6\x94\xaf\xe4\xbb\x98\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='Proj_name',
            field=models.CharField(max_length=50, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='project',
            name='landlord_account',
            field=models.CharField(max_length=20, verbose_name=b'\xe6\x88\xbf\xe4\xb8\x9c\xe8\xb4\xa6\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='project',
            name='landlord_account_bank',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\xbc\x80\xe6\x88\xb7\xe8\xa1\x8c'),
        ),
        migrations.AlterField(
            model_name='project',
            name='payment_period',
            field=models.CharField(max_length=4, verbose_name=b'\xe6\x94\xaf\xe4\xbb\x98\xe5\x91\xa8\xe6\x9c\x9f', choices=[(b'hy', b'\xe5\x8d\x8a\xe5\xb9\xb4'), (b'ye', b'\xe5\xb9\xb4\xe4\xbb\x98')]),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier_account',
            field=models.CharField(max_length=20, verbose_name=b'\xe4\xbe\x9b\xe5\xba\x94\xe5\x95\x86\xe8\xb4\xa6\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier_account_bank',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\xbc\x80\xe6\x88\xb7\xe8\xa1\x8c'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier_name',
            field=models.CharField(max_length=20, verbose_name=b'\xe4\xbe\x9b\xe5\xba\x94\xe5\x95\x86\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
