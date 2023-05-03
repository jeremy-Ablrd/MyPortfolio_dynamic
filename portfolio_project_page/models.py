from django.db import models
from django import forms
from django.core.validators import MinValueValidator
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.

class Page(models.Model):
    id_project = models.IntegerField(default=1, primary_key=True, validators=[MinValueValidator(1)])
    title_1 = models.CharField(max_length=100)  
    title_2 = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='card_images/', null=True)      # 'MEDIA_ROOT/card_images/'
    download_zip_images = models.FileField(upload_to='zip_images/', null=True)
    description = models.TextField()
    contents = RichTextField()
    
    slug = models.SlugField(unique=True, max_length=100, default=None)      # slug : il permet de créer l'url à partir du premier titre de la page généré.

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_1.split(" "))
        self.slug += f"-id{self.id_project}"
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.title_1