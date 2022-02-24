
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings

from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
    path('audio/', include('audio.urls')),
    path('video_satsang/', include('video.urls')),
    path('gallery/', include('gallery.urls')),
    path('humanitarian/', views.humanitarian, name='humanitarian'),
    path('mission_education/', views.misson_education, name='misson'),
    path('satsang_programs/', views.satsangs, name='satsangs'),
    path('children_welfare/', views.children,name='children'),
    path('community_service/', views.community, name='community')

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
 