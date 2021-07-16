from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazıçı")
    title = models.CharField(max_length=30,verbose_name="Başlıq")
    content = RichTextField(verbose_name="Mətin")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Hazırlandığı tarix")
    article_photo = ResizedImageField(size = [700,450],blank = True, null = True, verbose_name="Şəkil əlavə et")
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE,verbose_name="Meqale",related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="Ad")
    comment_content =models.CharField(max_length=400,verbose_name="Rəy")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']