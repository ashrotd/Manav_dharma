from django.db import models

# Create your models here.
class VideoSatsang(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.CharField(max_length=200)
    thumbnail_image = models.ImageField(upload_to='thumnails')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title