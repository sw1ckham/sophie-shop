from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_wordpress_templates(request):

    products = Product.objects.filter(category=1)

    context = {
        'products': products,
    }

    return render(request, 'products/wordpress_templates.html', context)


def all_wordpress_themes(request):

    products = Product.objects.filter(category=2)

    context = {
        'products': products,
    }

    return render(request, 'products/wordpress_themes.html', context)


def all_squarespace_templates(request):

    products = Product.objects.filter(category=4)

    context = {
        'products': products,
    }

    return render(request, 'products/squarespace_templates.html', context)


def all_squarespace_plugins(request):

    products = Product.objects.filter(category=3)

    context = {
        'products': products,
    }

    return render(request, 'products/squarespace_plugins.html', context)


def product_detail(request, product_id):
        """ A view to show individual product details """
        product = get_object_or_404(Product, pk=product_id)

        context = {
            'product': product,
        }

        return render(request, 'products/product_detail.html', context)