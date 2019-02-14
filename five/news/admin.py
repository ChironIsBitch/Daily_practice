from django.contrib import admin
import xadmin
from .models import *
# Register your models here.

class NewsAdmin(object):
    list_display = ('id', 'title')
    style_fields = {"content":"ueditor"}
xadmin.site.register(News, NewsAdmin)