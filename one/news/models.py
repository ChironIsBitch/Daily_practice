from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    c_time = models.DateTimeField(auto_now_add=True)
    l_time = models.DateTimeField(auto_now=True)
