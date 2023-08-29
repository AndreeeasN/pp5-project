from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, ProductTag


def all_products(request):
    """
    View that displays all products, including sorted/filtered queries.
    """
    products = Product.objects.all()
    query = None
    category = None
    tags = None
    sort = None
    direction = None

    if request.GET:
        # Sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Category Filter
        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name=category)
            category = Category.objects.filter(name=category)

        # Tag Filter
        if 'tags' in request.GET:
            tags = request.GET['tags'].split(',')
            products = products.filter(product_tags__name__in=tags).distinct
            tags = ProductTag.objects.filter(name__in=tags)

        # Search Filter
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.warning(
                    request,
                    "No search text entered."
                    )
                return redirect(reverse('products'))

            # Searches name, description and tags
            queries = (
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(product_tags__name__icontains=query)
                )
            products = products.filter(queries).distinct

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'current_category': category,
        'current_tags': tags,
        'search_term': query,
        'current_sorting': current_sorting,
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
