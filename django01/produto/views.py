from django.shortcuts import render
from produto.models import Produto

def shopAll(request):
    fragrance = Produto.objects.filter(categoria=1).order_by('nome')
    bathb = Produto.objects.filter(categoria=2).order_by('nome')
    skin = Produto.objects.filter(categoria=3).order_by('nome')
    cheeks = Produto.objects.filter(categoria=4).order_by('nome')
    eyes = Produto.objects.filter(categoria=5).order_by('nome')
    lips = Produto.objects.filter(categoria=6).order_by('nome')
    face = Produto.objects.filter(categoria=7).order_by('nome')
    palettes = Produto.objects.filter(categoria=8).order_by('nome')
    featured = Produto.objects.filter(categoria=9).order_by('nome')
    return render(request, 'produto/shopAll.html', { 'featured': featured, 'fragrances': fragrance,'bathbody': bathb, 
    'skincare': skin, 'face': face, 'eyes': eyes, 'lips': lips, 'cheeks': cheeks, 'palettes': palettes})

def skincare(request):
    produtos = Produto.objects.filter(categoria=3).order_by('nome')
    print(produtos)
    return render(request, 'produto/skincare.html', { 'skincare': produtos })

def fragrances(request):
    produtos = Produto.objects.filter(categoria=1).order_by('nome')
    print(produtos)
    return render(request, 'produto/fragrances.html', { 'fragrances': produtos })

def bathbody(request):
    produtos = Produto.objects.filter(categoria=2).order_by('nome')
    print(produtos)
    return render(request, 'produto/bath&body.html', { 'bathbody': produtos })

def makeup(request):
    cheeks = Produto.objects.filter(categoria=4).order_by('nome')
    eyes = Produto.objects.filter(categoria=5).order_by('nome')
    lips = Produto.objects.filter(categoria=6).order_by('nome')
    face = Produto.objects.filter(categoria=7).order_by('nome')
    palettes = Produto.objects.filter(categoria=8).order_by('nome')
    return render(request, 'produto/makeup.html', { 'face': face, 'eyes': eyes, 'lips': lips, 'cheeks': cheeks, 'palettes': palettes})
