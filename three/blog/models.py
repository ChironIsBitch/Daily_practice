from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    content = UEditorField(verbose_name="文章内容")
