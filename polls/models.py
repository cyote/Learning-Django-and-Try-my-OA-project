# coding:utf8
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        #  timezone.now 当前时间， datetime.timedelta(days=1)选定时间的前一天，意思是如果这个日期是在昨天后产生的，就是最近发布的。
    was_published_recently.admin_oder_field = 'pub_date' # 按发布日期排序
    was_published_recently.boolean = True  # 打钩表示True
    was_published_recently.short_description = 'Published recently?'  # 更改字段（原函数名）为指示的文字

    def __unicode__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text


