from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200, verbose_name='主题名称')
    date_added = models.DateTimeField(auto_now=True, editable=False, verbose_name='创建时间')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='创建人')

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

    class Meta:
        """定义数据表名称"""
        db_table = "topic"
        verbose_name = verbose_name_plural = '主题'


class Entry(models.Model):
    """某个主题的特定知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='选择主题')
    title = models.CharField(max_length=50,default='无标题', verbose_name='标题')
    text = models.TextField(verbose_name='内容')
    date_added = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    class Meta:
        db_table = 'entry'
        verbose_name = verbose_name_plural = '条目'

    def __str__(self):
        """返回默认显示"""
        return self.title




