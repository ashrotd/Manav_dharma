from django.contrib import admin
from .models import BlogModel
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('title',)}

admin.site.register(BlogModel, BlogAdmin)