from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """
    View that displays all products, including sorted/filtered queries.
    """
    products = Product.objects.all()
    query = None

    # If a search is being made
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.warning(
                    request,
                    "No search text entered, showing all products"
                    )
                return redirect(reverse('products'))

        # Searches name, description and tags
        queries = (
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(product_tags__name__icontains=query)
            )
        products = products.filter(queries).distinct

    context = {
        'products': products,
        'search_term': query,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    View that displays product details of product with specified id
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
