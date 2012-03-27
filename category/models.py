#coding=utf-8
from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=32,verbose_name=u'名称',unique=True)
    remark=models.TextField(verbose_name=u'备注')
    def __unicode__(self):
        return self.name
