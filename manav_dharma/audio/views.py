from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import BhajansAudio
from django.core.paginator import Paginator
# Create your views here.
def audio(request):
    bhajans = BhajansAudio.objects.all()
    paginator = Paginator(bhajans,9)
    page = request.GET.get('page')
    paged_bhajans = paginator.get_page(page)
    context = {'bhajans':paged_bhajans}
    return render(request,'audio.html',context)