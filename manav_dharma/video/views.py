from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import VideoSatsang

# Create your views here.
def video(request):
    videos = VideoSatsang.objects.all()
    context = {'video':videos}
    return render(request,'video.html',context)