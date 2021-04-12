from django.shortcuts import render
from .models import image

# Create your views here.

def display_image(request):
    images = image.objects.all()
    context = {
        "photos": images
    }
    return render(request, "index.html", context)
