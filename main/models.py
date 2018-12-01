from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

    class Meta:
        """定义数据表名称"""
        db_table = "topic"


class Entry(models.Model):
    """某个主题的特定知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,default='无标题')
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'entry'
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回默认显示"""
        return self.title




