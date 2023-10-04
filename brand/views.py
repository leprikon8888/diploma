from django.shortcuts import render
from .models import BrandShapka, Poslugi
# Create your views here.


def main_page(request):
    categories = BrandShapka.objects.filter(is_visible=True)
    return render(request, 'main.html', context={'categories': categories})


def poslugi(request):
    categories = Poslugi.objects.filter(is_visible=True)
    return render(request, 'main.html', context={'categories': categories})
