from django.shortcuts import render
from .models import GalleryModel
from django.core.paginator import Paginator

# Create your views here.
def gallery(request):
    gallery = GalleryModel.objects.all()
    paginator = Paginator(gallery,9)
    page = request.GET.get('page')
    paged_gallery = paginator.get_page(page)
    context = {'gallery':paged_gallery}
    return render(request,'gallery.html',context)
