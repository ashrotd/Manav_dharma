from django.db import models

# Create your models here.
class BhajansAudio(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='audio/')
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name