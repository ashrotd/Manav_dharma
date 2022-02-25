from django.db import models

# Create your models here.
class BhajansAudio(models.Model):
    file = models.FileField(upload_to='audio/')
    created_date = models.DateTimeField(auto_now_add=True)
    