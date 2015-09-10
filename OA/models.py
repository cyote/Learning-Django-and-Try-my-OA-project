# coding:utf8
from django.db import models

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

    #按校区分类的项目

    class Meta:
        verbose_name = '校区项目'

    Proj_name = models.CharField('项目名称', max_length=100)
    adr_txt = models.CharField('地址', max_length=100)
    sign_date = models.DateField('签约日期')
    rent = models.IntegerField('租金', default =0)
    landlord = models.CharField('房东名称', max_length=100)
    landlord_account = models.BigIntegerField('房东账号')
    landlord_account_bank = models.CharField('开户行', max_length=200)
    payment_period = models.CharField('支付周期', max_length=50)
    deposit = models.IntegerField('租赁保证金', default=0)

    # deco_contract = models.ManyToManyField(Decoration_contract)
    # ac_contract = models.ManyToManyField(Ac_contract)

    def __unicode__(self):
        return self.Proj_name


class SupplierType(models.Model):

    class Meta:
        verbose_name = '供应商类型'

    supplier_Type = models.CharField('供应商类型', max_length=50)

    def __unicode__(self):
        return self.supplier_Type


class Supplier(models.Model):

    #供应商


    class Meta:
        verbose_name = '供应商'

    supplier_name = models.CharField('供应商名称', max_length=100)
    supplier_account = models.BigIntegerField('供应商账号')
    supplier_account_bank = models.CharField('开户行', max_length=200)
    supplier_Type = models.ForeignKey(SupplierType)

    def __unicode__(self):
        return self.supplier_name



class DecorationContract(models.Model):

    #装修合同

    class Meta:
        verbose_name = '装修工程'

    project_name = models.ForeignKey(Project, verbose_name='校区')
    proj_type = models.ForeignKey(SupplierType, verbose_name='项目类别')
    supplier = models.ForeignKey(Supplier, verbose_name='供应商')
    Proj_Name = models.CharField('项目名称', max_length=100)
    sign_date = models.DateField('签约日期')
    price = models.IntegerField('合约总价', default=0)
    first_payment = models.IntegerField('首期支付', default=0)
    Sec_payment = models.IntegerField('二期支付', default=0)
    Thrd_payment = models.IntegerField('三期支付', default=0)
    Fourth_payment = models.IntegerField('四期支付', default=0)
    Fifth_payment = models.IntegerField('五期支付', default=0)

    def __unicode__(self):
        return self.Proj_Name