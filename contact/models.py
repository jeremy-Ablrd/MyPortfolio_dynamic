from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(verbose_name ='Nom et Prénom', max_length=100)
    email = models.EmailField(verbose_name='E-mail')
    society = models.CharField(verbose_name='Société', max_length=100)
    message = models.TextField(verbose_name='Message')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name