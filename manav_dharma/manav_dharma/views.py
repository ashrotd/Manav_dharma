
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogModel
from video.models import VideoSatsang
from audio.models import BhajansAudio
def home(request):
    blog = BlogModel.objects.all().order_by('-created_date')[:3]
    videos = VideoSatsang.objects.all().order_by('-created_date')[:2]
    bhajans = BhajansAudio.objects.all().order_by('-created_date')[:3]
    context = {'blog':blog,'videos':videos,'bhajans':bhajans}
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')



def humanitarian(request):
    return render(request,'events/humanitarian.html')

def misson_education(request):
    return render(request,'events/misson_education.html')

def satsangs(request):
    return render(request,'events/satsangs.html')

def children(request):
    return render(request,'events/children_welfare.html')

def community(request):
    return render(request,'events/community.html')