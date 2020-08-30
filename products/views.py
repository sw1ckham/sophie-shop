from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

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


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)