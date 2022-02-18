from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import VideoSatsang
from django.core.paginator import Paginator

# Create your views here.
def video(request):
    videos = VideoSatsang.objects.all()
    paginator = Paginator(videos,9)
    page = request.GET.get('page')
    paged_videos = paginator.get_page(page)
    context = {'video':paged_videos}
    return render(request,'video.html',context)