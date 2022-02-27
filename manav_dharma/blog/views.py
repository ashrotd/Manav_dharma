from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogModel
from django.core.paginator import Paginator

# Create your views here.
def blog(request):
    blogs = BlogModel.objects.all()
    paginator = Paginator(blogs,9)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    context = {'blogs':paged_blogs}
    
    
    return render(request,'blog.html',context)

def blog_detail(request, blog_slug):
    try:
        single_blog = BlogModel.objects.get(slug=blog_slug)
    except Exception as e:
        raise e
    recent_blog = BlogModel.objects.all().order_by('-created_date')[:5]
    day = single_blog.created_date.strftime("%b")
    context = {'single_blog':single_blog, 'recent_blog':recent_blog,'day':day}
    return render(request,'blog_detail.html',context)