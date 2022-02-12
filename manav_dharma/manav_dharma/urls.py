
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings

from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog', include('blog.urls')),
    path('audio', include('audio.urls')),
    path('video_satsang', include('video.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
 