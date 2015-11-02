# coding:utf8
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
'''




class Project(models.Model):

    # 按校区分类的项目
    class Meta:
        verbose_name_plural = '校区列表'

    payment_period_list = (

        ('hy', '半年'),
        ('ye', '年付'),
    )

    proj_code = models.CharField('项目编号', max_length=3)
    Proj_name = models.CharField('项目名称', max_length=50)
    adr_txt = models.CharField('地址', max_length=100)
    sign_date = models.DateField('签约日期')
    rent = models.IntegerField('租金', default =0)
    landlord = models.CharField('房东名称', max_length=100)
    landlord_account = models.CharField('房东账号', max_length=20)
    landlord_account_bank = models.CharField('开户行', max_length=50)
    payment_period = models.CharField('支付周期',choices=payment_period_list, max_length=4)
    deposit = models.IntegerField('租赁保证金', default=0)
    first_pay = models.IntegerField('首期支付', default=0)
    first_pay_date = models.DateField('首期支付时间')
    sec_pay = models.IntegerField('二期支付', default=0)
    sec_pay_date = models.DateField('二期支付时间')
    thd_pay = models.IntegerField('三期支付', default=0)
    thd_pay_date = models.DateField('三期支付时间')
    fou_pay = models.IntegerField('四期支付', default=0)
    fou_pay_date = models.DateField('四期支付时间')
    fif_pay = models.IntegerField('五期支付', default=0)
    fif_pay_date = models.DateField('五期支付时间')
    six_pay = models.IntegerField('六期支付', default=0)
    six_pay_date = models.DateField('六期支付时间')
    sev_pay = models.IntegerField('七期支付', default=0)
    sev_pay_date = models.DateField('七期支付时间')
    eit_pay = models.IntegerField('八期支付', default=0)
    eit_pay_date = models.DateField('八期支付时间')
    nin_pay = models.IntegerField('九期支付', default=0)
    nin_pay_date = models.DateField('九期支付时间')
    ten_pay = models.IntegerField('十期支付', default=0)
    ten_pay_date = models.DateField('十期支付时间')
    # deco_contract = models.ManyToManyField(Decoration_contract)
    # ac_contract = models.ManyToManyField(Ac_contract)

    def __unicode__(self):
        return self.Proj_name


class SupplierType(models.Model):

    class Meta:
        verbose_name_plural = '供应商类型'

    supplier_Type = models.CharField('供应商类型', max_length=50)

    def __unicode__(self):
        return self.supplier_Type


class Supplier(models.Model):

    # 供应商
    class Meta:
        verbose_name_plural = '供应商信息'

    supplier_name = models.CharField('供应商名称', max_length=20)
    supplier_account = models.CharField('供应商账号', max_length=20)
    supplier_account_bank = models.CharField('开户行', max_length=50)
    supplier_Type = models.ForeignKey(SupplierType, verbose_name='供应商类型')

    def __unicode__(self):
        return self.supplier_name


class DecorationContract(models.Model):
    # 装修合同
    class Meta:
        verbose_name_plural = '装修工程列表'

    school_name = models.ForeignKey(Project, verbose_name='校区')
    proj_type = models.ForeignKey(SupplierType, verbose_name='项目类别')
    supplier = models.ForeignKey(Supplier, verbose_name='供应商')
    proj_name = models.CharField('项目名称', max_length=20)
    sign_date = models.DateField('签约日期')
    price = models.IntegerField('合约总价', default=0,)
    first_payment = models.IntegerField('首期支付', default=0)
    first_payment_date = models.DateField('首期支付时间')
    sec_payment = models.IntegerField('二期支付', default=0)
    sec_payment_date = models.DateField('二期支付时间')
    thd_payment = models.IntegerField('三期支付', default=0)
    thd_payment_date = models.DateField('三期支付时间')
    fou_payment = models.IntegerField('四期支付', default=0)
    fou_payment_date = models.DateField('四期支付时间')
    fif_payment = models.IntegerField('五期支付', default=0)
    fif_payment_date = models.DateField('五期支付时间', null=True)





    def __unicode__(self):
        return self.proj_name

