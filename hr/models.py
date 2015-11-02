# coding:utf8
from django.db import models
from OA.models import Project


# Create your models here.
class Employee(models.Model):

    class Meta:
        verbose_name_plural = '员工信息'

    position_list = (
        ('SD', '校长'),
        ('ASD', '助理校长'),
        ('DOS', '教学副校长'),
        ('CCM', '咨询经理'),
        ('CRM', '客服经理'),
        ('CCS', '咨询主管'),
        ('CRS', '客服主管'),
        ('TRM', '学科组长'),
        ('TRS', '学科带头人'),
        ('CC', '教育顾问'),
        ('CR', '班主任'),
        ('TR', '学科教师'),
        ('YWTR', '语文教师'),
        ('SXTR', '数学教师'),
        ('YYTR', '英语教师'),
        ('WLTR', '物理教师'),
        ('HXTR', '化学教师'),
        ('KXTR', '科学教师'),
        ('ZSDTR', '政史地教师'),
        ('QTTR', '其他教师'),
        ('TL', '出纳'),
        ('CP', '教务专员'),
        ('AD', '行政'),
        ('CL', '保洁'),
        ('LMS', '市场主管')
    )

    gender = (
        ('M', '男'),
        ('F', '女'),
    )

    diploma_list = (
        ('Dr', '博士'),
        ('Ma', '硕士'),
        ('Ba', '本科'),
        ('Sp', '专科'),
        ('ot', '其他'),
    )


    # user_index = models.SmallIntegerField('序号', )
    user_name = models.CharField('姓名', max_length=10)
    user_position = models.CharField('职位', choices=position_list, max_length=10)
    user_mail = models.EmailField('邮箱')
    user_workcode = models.CharField('工号', unique=True, default=0,max_length=12)
    user_school = models.ForeignKey(Project, verbose_name='校区', null=True)
    user_phonenumber = models.CharField('联系方式', max_length=11)
    user_salary = models.IntegerField('薪资', default=0, blank=True)
    user_arrivetime = models.DateField('到岗时间', null=True)
    user_ID = models.CharField('身份证号', unique=True, max_length=20, null=True)
    user_gender = models.CharField('性别', choices=gender, max_length=2)
    user_birthday = models.DateField('出生年月', null=True)
    user_diploma = models.CharField('最高学历', choices=diploma_list, default='Ba', max_length=10)
    user_graduate_colledge = models.CharField('毕业院校', max_length= 40)
    user_major = models.CharField('专业', max_length=20)

    def __unicode__(self):
        return self.user_name
