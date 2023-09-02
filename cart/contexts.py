from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings
from products.models import Product, ProductVariant


def cart_contents(request):
    """
    Context proccessor containing contents of shopping cart
    """
    cart_items = []
    total = 0
    product_count = 0
    delivery_threshold = settings.FREE_DELIVERY_THRESHOLD
    cart = request.session.get('cart', {})

    for item_key, item in cart.items():
        item_id = item['item_id']
        variant_id = item['variant_id']
        quantity = item['quantity']

        product = get_object_or_404(Product, pk=item_id)
        variant = None

        # If item has a size/variant add variant price
        if variant_id is not None:
            variant = get_object_or_404(ProductVariant, pk=variant_id)
            price = variant.variant_price
        else:
            price = product.price

        subtotal = price * quantity
        total += subtotal
        product_count += quantity

        cart_items.append({
            "item_key": item_key,
            'product': product,
            'variant': variant,
            'quantity': quantity,
            'price': price,
            'subtotal': subtotal,
        })

    if total < delivery_threshold:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = delivery_threshold - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': delivery_threshold,
        'grand_total': grand_total,
    }

    return context
