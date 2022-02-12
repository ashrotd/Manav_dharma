
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogModel

def home(request):
    blog = BlogModel.objects.all().order_by('-created_date')[:3]
    
    context = {'blog':blog}
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')