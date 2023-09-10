from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from products.forms import ProductForm
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
    # Products per page
    paginate_by = 24

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
            products = products.filter(
                product_tags__name__in=tags,
                product_tags__search_visible=True
                ).distinct()
            tags = ProductTag.objects.filter(
                name__in=tags,
                search_visible=True)

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
            products = products.filter(queries).distinct()

    current_sorting = f'{sort}_{direction}'

    # Pagination
    paginator = Paginator(products, paginate_by)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'products': products,
        'current_category': category,
        'current_tags': tags,
        'search_term': query,
        'current_sorting': current_sorting,
        'paginator': paginator,
        'page_obj': page_obj,
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


@login_required
def add_product(request):
    """
    Add a new product to the store
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            "Only superusers may add new products."
            )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(
                request,
                'Successfully added product!'
                )
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
                )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit an existing product
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            "Only superusers may edit products."
            )
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Successfully updated product!"
            )
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm(instance=product)

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete an existing product
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            "Only superusers may delete products."
            )
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()

    messages.success(
        request,
        "Successfully deleted product!"
    )
    return redirect(reverse('products'))
