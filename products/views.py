from django.shortcuts import render
from .models import Product

# Create your views here.

def all_wordpress_templates(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/wordpress_templates.html', context)


def all_wordpress_themes(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/wordpress_themes.html', context)


def all_squarespace_templates(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/squarespace_templates.html', context)


def all_squarespace_plugins(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/squarespace_plugins.html', context)