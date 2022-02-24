from statistics import mode
from django.db import models

# Create your models here.
class GalleryModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery', help_text='Recommended Size 370X370px')
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title