
from django.db import models
from ckeditor.fields import RichTextField
from django.urls.base import reverse

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=1000, unique=True)
    content = RichTextField(blank=True)
    slug = models.SlugField(max_length=1000, unique=True)
    image = models.ImageField(upload_to='blog', help_text="Recommended Size 350X260px")
    real_image = models.ImageField(upload_to='detail_blog', help_text="Used Inside a Blog")
    author = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('blog_detail', args=[self.slug])