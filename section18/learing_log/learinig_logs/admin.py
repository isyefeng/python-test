from django.contrib import admin

# Register your models here.

from learinig_logs.models import Topic,Entry

#添加Topic模块
admin.site.register(Topic)
#添加Entry模块
admin.site.register(Entry)
