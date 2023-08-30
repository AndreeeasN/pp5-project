from decimal import Decimal
from django.conf import settings


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    delivery_threshold = settings.FREE_DELIVERY_THRESHOLD

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
