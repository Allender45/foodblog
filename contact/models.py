from ckeditor.fields import RichTextField
from django.db import models


class ContactModel(models.Model):
    """
    Класс модели обратной связи
    """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + '-' + self.email


class ContactLink(models.Model):
    """
    Класс модели контактов
    """
    icon = models.FileField(upload_to='icons')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class About(models.Model):
    """
    Класс модели страницы О нас
    """
    text = RichTextField()
    mini_text = RichTextField()
    name = models.CharField(max_length=100, default='')


class Image(models.Model):
    """
    Класс моделей изображений на странице о нас
    """
    image = models.ImageField(upload_to='about')
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')
    alt = models.CharField(max_length=100, default='blank')


class Social(models.Model):
    """
    Класс модели цос сетей страницы о нас.
    """
    icon = models.FileField(upload_to='icons')
    name = models.CharField(max_length=200)
    link = models.URLField()
