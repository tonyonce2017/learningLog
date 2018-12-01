from django import forms
from .models import *


class TopicForm(forms.ModelForm):
    """主题表单管理"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}  # 不生成标签


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

