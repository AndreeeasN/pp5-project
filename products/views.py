from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    View that displays all products, including sorted/filtered queries.
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
