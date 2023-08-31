from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product, ProductVariant


def view_cart(request):
    """
    View that displays the contents of the shopping cart
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    View that adds the specified item to the shopping cart
    """
    quantity = int(request.POST.get('quantity'))
    variant_id = request.POST.get('variant')
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    item = get_object_or_404(Product, pk=item_id)
    printMsg = f'Added {quantity} {item.name}'

    # If base item has a variant
    if item.product_variants.count():
        # If user has selected a variant
        if (variant_id is not None):
            variant = get_object_or_404(ProductVariant, pk=int(variant_id))

            # If variant belongs to this product
            if variant in item.product_variants.all():
                cart_item_key = f'{item_id}_{variant_id}'
                printMsg += f' - {variant.friendly_name}'
            else:
                messages.warning(
                    request,
                    "Product does not come in the specified size/variant."
                    )
                return redirect(redirect_url)
        else:
            messages.warning(
                    request,
                    "Please select a valid size/variant."
                    )
            return redirect(redirect_url)
    else:
        cart_item_key = item_id

    cart_item = {
        'item_id': item_id,
        'variant_id': variant_id,
        'quantity': quantity,
    }

    # If item exists, increase by quantity
    if cart_item_key in cart:
        cart[cart_item_key]['quantity'] += quantity
    else:
        # Otherwise add cart_item to cart
        cart[cart_item_key] = cart_item

    # Updates cart and display success message
    request.session['cart'] = cart
    messages.success(request, printMsg)

    return redirect(redirect_url)
