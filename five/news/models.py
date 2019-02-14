from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    content = UEditorField(verbose_name="文章内容")
    # class Meta:
    #     verbose_name="新闻中心"
    #     verbose_name_plural = verbose_name
