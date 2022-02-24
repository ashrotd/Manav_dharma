from django.shortcuts import render
from .models import Contact
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone')
        contact.message = request.POST.get('message')
        contact.save()
        messages.success(request,'Thank You for the message')
        
    return render(request,'contact.html')