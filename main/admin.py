from django.contrib import admin
from main.models import *

# Register your models here.


admin.site.site_header = '学习笔记后台管理系统'
admin.site.site_title = '学习笔记'
admin.site.register(Topic)
admin.site.register(Entry)