from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='email_address', max_length=255)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=150, blank=True)

    def __str__(self):
        return self.name