from django.shortcuts import render
from produto.models import Produto

def index(request):
    featured = Produto.objects.filter(categoria=9).order_by('nome')
    print(featured)
    return render(request, 'index.html', { 'featured': featured })


def aboutUs(request):
    return render(request, 'aboutUs.html')
